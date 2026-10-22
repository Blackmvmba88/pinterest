# Estado de continuación

- Repositorio existente: Blackmvmba88/pinterest (público).
- Prioridad: cada material visual debe estar asociado a una canción concreta y sus metadatos.
- Restricción: reducir uso de Codex/ChatGPT; operaciones repetitivas locales, sin IA.
- Implementado: CLI Python/SQLite, canciones, materiales por SHA256, vínculos obligatorios,
  origen, autor opcional, etiquetas, propósito, explicación y porcentaje con método explícito.
- Operación real iniciada en Pinterest el 2026-10-22: se verificó acceso al editor
  de los pins propios. Metadatos editables: título, descripción y enlace.
- Prioridad explícita: los más virales primero. Ranking histórico disponible en
  exportación 2026-09-11/2026-10-11; validar cifras actuales en cada pin.
- Primer lote: cuatro pins recientes actualizados y verificados tras recarga.
- Lote viral: los tres primeros del ranking actualizados y verificados tras recarga.
  Cada uno tiene título, descripción, diez hashtags y una canción real verificada.
- Advertencia observada: Pinterest avisa que cambiar el enlace pierde métricas de
  engagement asociadas. Para los virales se mantuvo el campo de enlace y se incluyó
  la URL de la canción en la descripción; no equivale a un botón musical directo.
- Inventarios, ranking, respaldos antes/después y capturas quedan en data/ (local).
  Continuar desde data/viral-priority.json: 3 verificados, 47 pendientes del reporte;
  no es un inventario completo de la cuenta.
- Las relaciones musicales son nuevas selecciones editoriales por tema visual,
  no afirmaciones de portada oficial, autoría de imagen ni análisis del audio.
- Pendiente: conectar la salida del analizador existente con el CLI. El registro
  operativo de Pinterest está en JSON; no asumir integración automática con SQLite.
- Los datos reales permanecen locales en data/ y no se publican.
