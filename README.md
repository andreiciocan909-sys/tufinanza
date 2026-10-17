# TuFinanza

Sitio estático, sin frameworks ni dependencias. La guía de cuenta bancaria contiene texto provisional; revisa los fragmentos [VERIFICAR] antes de publicar.

## Añadir un artículo
1. Crea `articulos/tu-slug.html` siguiendo la estructura del artículo existente (incluye canonical, metadatos, JSON-LD, índice y marcadores de anuncio).
2. Añade una entrada con `title`, `slug`, `description` y `date` a `scripts/articles.json`.
3. Ejecuta `node scripts/generate.mjs` para regenerar portada y sitemap.

No requiere instalación de paquetes.
