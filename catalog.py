"""Local song-linked visual catalog. Python standard library only."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3


def connect(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute("PRAGMA foreign_keys=ON")
    db.executescript('''
        CREATE TABLE IF NOT EXISTS songs (
            id TEXT PRIMARY KEY, title TEXT NOT NULL, url TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS materials (
            sha256 TEXT PRIMARY KEY, filename TEXT NOT NULL,
            source_url TEXT NOT NULL, author TEXT, tags TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS links (
            sha256 TEXT REFERENCES materials(sha256),
            song_id TEXT REFERENCES songs(id), purpose TEXT NOT NULL,
            reason TEXT NOT NULL, score REAL, score_method TEXT,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (sha256, song_id, purpose));
    ''')
    return db


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', default='data/catalog.sqlite3')
    sub = parser.add_subparsers(dest='command', required=True)
    song = sub.add_parser('song', help='Register a song from your catalog')
    for field in ('id', 'title', 'url'):
        song.add_argument('--' + field, required=True)
    material = sub.add_parser('material', help='Register a file and its song relationship')
    material.add_argument('file', type=Path)
    for field in ('song-id', 'source-url', 'purpose', 'reason'):
        material.add_argument('--' + field, required=True)
    material.add_argument('--author')
    material.add_argument('--tag', action='append', default=[])
    material.add_argument('--score', type=float)
    material.add_argument('--score-method')
    sub.add_parser('export', help='Export all song-linked records as JSON')
    args = parser.parse_args()
    if args.command == 'material':
        if args.score is not None and not (0 <= args.score <= 100):
            parser.error('--score must be between 0 and 100')
        if args.score is not None and not args.score_method:
            parser.error('--score requires --score-method; do not invent percentages')
    with connect(args.db) as db:
        if args.command == 'song':
            db.execute('INSERT INTO songs VALUES (?, ?, ?) ON CONFLICT(id) DO UPDATE SET title=excluded.title, url=excluded.url',
                       (args.id, args.title, args.url))
        elif args.command == 'material':
            if not db.execute('SELECT 1 FROM songs WHERE id=?', (args.song_id,)).fetchone():
                parser.error('Register the song first using the song command')
            with args.file.open('rb') as stream:
                digest = hashlib.file_digest(stream, 'sha256').hexdigest()
            db.execute('INSERT INTO materials VALUES (?, ?, ?, ?, ?) ON CONFLICT(sha256) DO UPDATE SET filename=excluded.filename, source_url=excluded.source_url, author=excluded.author, tags=excluded.tags',
                       (digest, args.file.name, args.source_url, args.author, json.dumps(args.tag, ensure_ascii=False)))
            db.execute('''INSERT INTO links (sha256,song_id,purpose,reason,score,score_method)
                VALUES (?,?,?,?,?,?) ON CONFLICT(sha256,song_id,purpose) DO UPDATE SET
                reason=excluded.reason, score=excluded.score, score_method=excluded.score_method,
                updated_at=CURRENT_TIMESTAMP''',
                       (digest, args.song_id, args.purpose, args.reason, args.score, args.score_method))
            print(digest)
        else:
            db.row_factory = sqlite3.Row
            rows = db.execute('''SELECT m.*, s.id AS song_id, s.title AS song_title,
                s.url AS song_url, l.purpose, l.reason, l.score, l.score_method, l.updated_at
                FROM links l JOIN materials m ON m.sha256=l.sha256
                JOIN songs s ON s.id=l.song_id ORDER BY s.id,m.sha256,l.purpose''')
            records = [dict(row) for row in rows]
            for record in records:
                record['tags'] = json.loads(record['tags'])
            print(json.dumps(records, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
