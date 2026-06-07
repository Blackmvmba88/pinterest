# BLACKMAMBA CORE Roadmap

## Phase 0 — Repository Bootstrap

- [x] Create README
- [ ] Create strategic docs
- [ ] Create Python package structure
- [ ] Add initial CLI scanner
- [ ] Add tests
- [ ] Add CI

## Phase 1 — Local Image Library

Goal: build the first BlackMamba visual archive.

- [ ] Scan local folders
- [ ] Detect supported image files
- [ ] Compute SHA256 hashes
- [ ] Copy images into stable local cache
- [ ] Store metadata in SQLite
- [ ] Deduplicate exact matches

Deliverable:

```txt
Local Visual Library v0.1
```

## Phase 2 — Pinterest Taste Engine

Goal: ingest Pinterest as the first major taste source.

- [ ] Import Pinterest export JSON/CSV
- [ ] Store boards
- [ ] Store pins
- [ ] Store saves
- [ ] Store clicks and revisit events
- [ ] Cache pin images locally where permitted
- [ ] Weight clicks, saves, downloads, revisits, and reuse

Deliverable:

```txt
Pinterest Collector v0.1
```

## Phase 3 — Vision Engine / BM-Eye

Goal: make visual