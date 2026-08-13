# -*- coding: utf-8 -*-
"""
Delad markdown→html-konvertering och sidmall för de utskrivbara dokumenten.

Används av parm.py (hela lagpärmen i en fil) och doc.py (fristående dokument).
Ligger här för att konverteringen ska finnas på ETT ställe — samma regel som gäller
för övningarna: en källa, flera utskrifter.

Källfilerna använder bara: rubriker (#..####), tabeller, punkt- och nummerlistor,
> citat, ---, **fet**, *kursiv*, `kod` och [länk](mål).
"""
import re, html

esc = html.escape


# ---------------------------------------------------------------- konvertering
def inline(t):
    t = esc(t)
    t = re.sub(r'`([^`]+)`', r'<span class="mono">\1</span>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<i>\1</i>', t)
    return t


def _cells(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


#: en rad som bryter av en listpunkt i stället för att fortsätta den
_BREAKS = re.compile(r'^(#{1,4}\s|[-*]\s|\d+\.\s|>|\||---$|```)')


def _list(lines, i, itempat):
    """Samla listpunkter. En rad som varken är tom eller startar något nytt
    hör till föregående punkt — annars bryts **fet text** som radbrutits."""
    items = []
    while i < len(lines):
        s = lines[i].strip()
        if re.match(itempat, s):
            items.append(re.sub(itempat, '', s)); i += 1
            continue
        if items and s and not _BREAKS.match(s):
            items[-1] += ' ' + s; i += 1
            continue
        break
    return items, i


def md(text, drop_title=True):
    """→ (titel, undertitel, lede, brödtext-html)."""
    lines = text.replace('\r\n', '\n').split('\n')
    title = subtitle = lede = ""

    i = 0
    if drop_title:
        while i < len(lines):
            L = lines[i].strip()
            if not L:
                i += 1
                continue
            if L.startswith('# ') and not title:
                title = L[2:].strip(); i += 1; continue
            if L.startswith('## ') and title and not subtitle:
                subtitle = L[3:].strip(); i += 1; continue
            if L.startswith('*') and L.endswith('*') and not L.startswith('**') and title and not lede:
                lede = L.strip('*').strip(); i += 1
                while i < len(lines) and lines[i].strip().startswith('*') \
                        and lines[i].strip().endswith('*') and not lines[i].strip().startswith('**'):
                    lede += ' ' + lines[i].strip().strip('*').strip(); i += 1
                continue
            if L == '---' and title:
                i += 1
            break

    out, para = [], []

    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    while i < len(lines):
        L = lines[i]
        s = L.strip()

        if not s:
            flush(); i += 1; continue

        if s == '---':
            flush(); out.append('<hr>'); i += 1; continue

        m = re.match(r'^(#{2,4})\s+(.*)$', s)
        if m:
            flush()
            lvl = len(m.group(1))
            tag = {2: 'h3', 3: 'h4', 4: 'h5'}[lvl]
            cls = {2: 'mh2', 3: 'mh3', 4: 'mh4'}[lvl]
            out.append(f'<{tag} class="{cls}">{inline(m.group(2))}</{tag}>')
            i += 1; continue

        if s.startswith('> '):
            flush()
            q = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                q.append(lines[i].strip().lstrip('>').strip()); i += 1
            q = [x for x in q if x]
            out.append('<blockquote>' + ' '.join(inline(x) for x in q) + '</blockquote>')
            continue

        if s.startswith('|'):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(_cells(lines[i])); i += 1
            if len(rows) >= 2 and all(re.fullmatch(r':?-{2,}:?', c) or c == '' for c in rows[1]):
                head, bodyrows = rows[0], rows[2:]
            else:
                head, bodyrows = None, rows
            t = ['<table>']
            if head:
                t.append('<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead>')
            t.append('<tbody>')
            for r in bodyrows:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table>')
            out.append(''.join(t))
            continue

        if re.match(r'^[-*]\s+', s):
            flush()
            items, i = _list(lines, i, r'^[-*]\s+')
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>')
            continue

        if re.match(r'^\d+\.\s+', s):
            flush()
            items, i = _list(lines, i, r'^\d+\.\s+')
            out.append('<ol>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ol>')
            continue

        if s.startswith('```'):
            flush(); i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            i += 1
            out.append('<pre>' + esc('\n'.join(code)) + '</pre>')
            continue

        para.append(s); i += 1

    flush()
    return title, subtitle, lede, ''.join(out)


# ---------------------------------------------------------------- css
EXTRA_CSS = """
/* ---- markdown-typografi ---- */
.chap h3.mh2{font-size:clamp(24px,3.4vw,32px);text-transform:uppercase;font-weight:600;
  margin:44px 0 6px;padding-bottom:6px;border-bottom:1px solid var(--line);color:var(--blue)}
.chap h4.mh3{font-family:'Oswald',sans-serif;font-size:21px;text-transform:uppercase;
  font-weight:500;letter-spacing:.03em;margin:30px 0 4px}
.chap h5.mh4{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--copper);margin:24px 0 4px;font-weight:700}
.chap p{max-width:74ch;margin:0 0 13px;font-size:16.5px}
.chap p.lede{margin-bottom:6px}
.chap p.note{font-style:italic;color:var(--grey);font-size:15.5px;max-width:70ch;margin:0 0 30px}
.chap ul,.chap ol{max-width:74ch;margin:0 0 15px;padding-left:22px}
.chap li{margin-bottom:6px;font-size:16.5px}
.chap blockquote{margin:20px 0;padding:15px 22px;background:var(--card);
  border-left:4px solid var(--copper);border-top:1px solid var(--line);
  border-right:1px solid var(--line);border-bottom:1px solid var(--line);
  border-radius:0 4px 4px 0;font-size:18px;max-width:74ch}
.chap blockquote b{color:var(--blue)}
.chap hr{border:0;border-top:1px solid var(--line);margin:34px 0}
.chap pre{background:var(--card);border:1px solid var(--line);border-radius:4px;
  padding:14px 16px;font-family:'IBM Plex Mono',monospace;font-size:13px;overflow-x:auto}
.chap thead th{position:static}
.chap .dgm{width:100%;height:auto;display:block}

/* diagramruta i löptext */
.fig{background:var(--card);border:1px solid var(--line);border-radius:4px;
  padding:16px 18px 12px;margin:22px 0;max-width:560px}
.fig .cap{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--copper);font-weight:700;margin-bottom:10px}
.fig .exp{font-size:14.5px;color:#3A4340;margin:10px 0 0;max-width:none}
.figrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin:22px 0}
.figrow .fig{margin:0;max-width:none}

/* ---- omslag ---- */
.cover{background:var(--blue);color:#fff;padding:64px 0 0;border-bottom:9px solid var(--copper)}
.cover .wrap{padding-bottom:52px}
.cover h1{font-size:clamp(46px,10vw,110px);line-height:.86;text-transform:uppercase;
  font-weight:600;letter-spacing:-.01em}
.cover h1 em{font-style:normal;-webkit-text-stroke:1.5px var(--copper);color:transparent}
.cover .sub{max-width:60ch}
.cover .trio{display:flex;gap:0;margin-top:38px;border-top:1px solid rgba(255,255,255,.28)}
.cover .trio div{flex:1;padding:20px 18px 6px;border-right:1px solid rgba(255,255,255,.28)}
.cover .trio div:last-child{border-right:0}
.cover .trio strong{display:block;font-family:'Oswald',sans-serif;font-size:25px;
  text-transform:uppercase;font-weight:600;letter-spacing:.03em}
.cover .trio span{font-size:14.5px;color:#BCD2E2;display:block;margin-top:5px;line-height:1.4}

/* ---- innehåll ---- */
.toc{margin:34px 0 0;border-top:2px solid var(--ink)}
.tocrow{display:flex;align-items:baseline;gap:18px;padding:13px 4px;
  border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.tocrow:hover{background:var(--sand)}
.tocnum{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--copper);
  letter-spacing:.14em;font-weight:700}
.toctitle{font-family:'Oswald',sans-serif;font-size:24px;text-transform:uppercase;
  font-weight:500;letter-spacing:.02em}

/* ---- utskrift / PDF ---- */
@page{size:A4;margin:15mm 13mm 16mm}
@media print{
  nav{display:none!important}
  .noprint{display:none!important}
  body{background:#fff;font-size:10.2pt;line-height:1.42}
  .wrap{max-width:none;padding:0}
  .cover{background:#fff;color:var(--ink);border-bottom:4px solid var(--copper);
    padding-top:8mm;break-after:page;page-break-after:always}
  .cover h1{color:var(--ink);font-size:58pt}
  .cover h1 em{-webkit-text-stroke:1pt var(--copper);color:transparent}
  .cover .sub,.cover .eyebrow{color:var(--ink)}
  .cover .trio{border-top:1px solid var(--line)}
  .cover .trio div{border-right:1px solid var(--line)}
  .cover .trio span{color:var(--grey)}
  #innehall{break-after:page;page-break-after:always}
  section.chap{break-before:page;page-break-before:always;padding-top:0}
  section.chap.nobreak{break-before:auto;page-break-before:auto}
  .shead{border-bottom:2px solid var(--ink)}
  .shead h2{font-size:26pt}
  .ex,.ses,.call,.pcard,blockquote,.key,.fig{break-inside:avoid;page-break-inside:avoid}
  tr,li{break-inside:avoid;page-break-inside:avoid}
  thead{display:table-header-group}
  h2,h3,h4,h5,.wk{break-after:avoid;page-break-after:avoid}
  .ex-fig{background:#fff;border-right:1px solid var(--line)}
  .exgrid{gap:10px}
  a{color:var(--ink);text-decoration:none}
  .chap p,.chap li,.chap ul,.chap ol,.chap blockquote{max-width:none}
  table{font-size:9pt}
  .ex-body p,.cp li{font-size:9.4pt}
  footer{break-before:page;page-break-before:always}
}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700'
         '&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400'
         '&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">')


def shell(title, css, eyebrow, h1a, h1b, sub, trio, body, footer, nav=""):
    """Standardsidan: omslag, ev. nav, innehåll, sidfot."""
    triohtml = "".join(
        f'<div><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in trio)
    navhtml = f'<nav class="noprint"><div class="wrap">{nav}</div></nav>' if nav else ''
    return f'''<!DOCTYPE html>
<html lang="sv"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
{FONTS}
<style>{css}{EXTRA_CSS}</style></head><body>

<header class="cover"><div class="wrap">
<div class="eyebrow">{esc(eyebrow)}</div>
<h1>{esc(h1a)}<em>{esc(h1b)}</em></h1>
<div class="sub">{sub}</div>
{f'<div class="trio">{triohtml}</div>' if trio else ''}
</div></header>

{navhtml}

<div class="wrap">
{body}
<footer>{footer}</footer>
</div></body></html>'''
