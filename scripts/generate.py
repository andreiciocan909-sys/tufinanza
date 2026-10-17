#!/usr/bin/env python3
"""Genera index.html y sitemap.xml desde scripts/articles.json."""
from pathlib import Path
import json
from html import escape
ROOT = Path(__file__).resolve().parent.parent
articles = json.loads((ROOT / 'scripts/articles.json').read_text(encoding='utf-8'))
def e(value): return escape(str(value), quote=True)
cards = '\n'.join(f'<article class="card"><h2><a href="articulos/{e(a["slug"])}.html">{e(a["title"])}</a></h2><p>{e(a["description"])}</p><p class="meta"><time datetime="{e(a["date"])}">{e(a["date"])}</time></p></article>' for a in articles)
page = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>TuFinanza | Finanzas personales para jóvenes</title><meta name="description" content="Guías claras de finanzas personales para jóvenes en España."><link rel="canonical" href="https://tufinanza.eu/"><meta property="og:type" content="website"><meta property="og:site_name" content="TuFinanza"><meta property="og:title" content="TuFinanza | Finanzas personales para jóvenes"><meta property="og:description" content="Guías claras de finanzas personales para jóvenes en España."><meta property="og:url" content="https://tufinanza.eu/"><link rel="stylesheet" href="css/style.css"><!-- Script de banner de cookies (Cookiebot o Complianz): añadir aquí cuando esté configurado. --><!-- Script de AdSense: añadir aquí cuando se disponga de cuenta e ID. --></head><body><header class="site-header"><div class="header-inner"><a class="brand" href="index.html">TuFinanza</a><nav class="nav" aria-label="Navegación principal"><a href="index.html">Inicio</a><a href="#articulos">Artículos</a><a href="contacto.html">Contacto</a></nav></div></header><main class="container"><section class="hero"><div class="eyebrow">Finanzas personales, paso a paso</div><h1>Tu dinero, con más claridad</h1><p class="lead">Guías prácticas para empezar a tomar decisiones financieras informadas en España.</p></section><section id="articulos"><h2>Artículos</h2><div class="article-list">{cards}</div></section></main><footer class="site-footer"><div class="footer-inner"><nav class="footer-links" aria-label="Enlaces legales"><a href="privacidad.html">Privacidad</a><a href="aviso-legal.html">Aviso legal</a><a href="contacto.html">Contacto</a></nav><p>Contenido informativo, no asesoramiento financiero.</p><p>© 2026 TuFinanza</p></div></footer></body></html>'''
(ROOT / 'index.html').write_text(page, encoding='utf-8')
static = ['', 'privacidad.html', 'aviso-legal.html', 'contacto.html']
entries = ''.join(f'  <url><loc>https://tufinanza.eu/{p}</loc></url>\n' for p in static)
entries += ''.join(f'  <url><loc>https://tufinanza.eu/articulos/{e(a["slug"])}.html</loc><lastmod>{e(a["date"])}</lastmod></url>\n' for a in articles)
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries + '</urlset>\n', encoding='utf-8')
print(f'Generados index.html y sitemap.xml con {len(articles)} artículo(s).')
