# Pinterest Taste Engine

Personal Creative Intelligence System for Iyari Cancino Gomez, artistically known as Iyari Gomez, under BlackMamba RECORDS.

This project learns from Pinterest saves, clicks, downloads, local images, prompts, covers, and creative metadata to build a living creative DNA model.

## Core laws

1. Preserve identity: never dilute the creative identity of Iyari Gomez and BlackMamba RECORDS.
2. Amplify identity: detect, strengthen, and expand patterns compatible with the existing BlackMamba aesthetic.

## Catálogo local: material → canción

Primera implementación: Python 3.11 o superior, SQLite y cero dependencias o llamadas de IA.
Cada material requiere una canción registrada, origen, uso previsto y explicación del vínculo.
Conserva autor (si se conoce), etiquetas, nombre del archivo y SHA256. El mismo contenido
no se duplica, aunque puede relacionarse con varias canciones o usos.

```sh
python3 catalog.py song --id tema-001 --title 'Mi canción' --url 'https://soundcloud.com/tu-cuenta/tu-tema'
python3 catalog.py material /ruta/imagen.jpg --song-id tema-001 --source-url 'https://www.pinterest.com/pin/ID/' --purpose portada --reason 'Comparte la atmósfera nocturna de la canción' --tag nocturno
python3 catalog.py export > data/catalog-export.json
```

Los datos quedan en `data/catalog.sqlite3`, excluidos de Git. Respaldar la base y los
archivos originales: el catálogo registra metadatos, no copia las imágenes.
Los ejemplos son ilustrativos; no representan canciones ni pins verificados.

El porcentaje es opcional. Si se registra con `--score 85`, exige
`--score-method 'evaluación manual: afinidad visual con la canción'`.
No se genera ni se presenta como probabilidad o confianza automática.

## Ahorro de uso

Registrar, consultar y exportar funciona localmente sin Codex/ChatGPT ni APIs.
Los registros guardados se reutilizan; esto no cambia las cuotas de Codex.
No hay aún análisis automático, sincronización con Pinterest ni caché de respuestas
de modelos. Antes de añadirlos, la clave de caché deberá incluir contenido,
canción, versión del modelo y versión de instrucciones para evitar resultados obsoletos.

## Siguiente entrega

Conectar el catálogo musical real y la salida del análisis existente a este registro.
El repositorio no incluye todavía ese analizador ni acceso a una cuenta de Pinterest.
