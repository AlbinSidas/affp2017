# -*- coding: utf-8 -*-
"""
Bygger ALLT: html-filerna, de fyra PDF:erna, och kontrollerar resultatet.

    cd _bygg
    python bygg-allt.py

Kör det här i stället för skripten ett och ett. Det finns av ett skäl: när PDF-steget
körts för hand har det tyst misslyckats och lämnat kvar gamla PDF:er som såg färdiga ut.
Skriptet jämför därför tidsstämplar och skriker om något är inaktuellt.

Avslutar med kod 1 om någon kontroll faller. Ingen utskick förrän det står ALLT OK.
"""
import os, re, sys, glob, subprocess, time

# Windows-konsolen är cp1252 och kvävs på å, ä och ö. Byt till utf-8 direkt.
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

STEG = ['build.py', 'bank.py', 'matguide.py', 'parm.py', 'doc.py', 'index.py']

PDF = [
    ('LAGPARMEN.html',        'Lagparmen.pdf'),
    ('09-positionsspel.html', 'Positionsspel.pdf'),
    ('10-till-er-hemma.html', 'Till-er-hemma.pdf'),
    ('07-matguide.html',      'Matguide.pdf'),
]

CHROME = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
]

fel = []


def kör(cmd, cwd, vad):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        fel.append('%s misslyckades (kod %d): %s' % (vad, r.returncode, (r.stderr or '')[-400:]))
        return None
    return (r.stdout or '').strip()


print('== html ==')
for s in STEG:
    ut = kör([sys.executable, s], HERE, s)
    if ut is not None:
        print('  %-14s %s' % (s, ut.splitlines()[-1] if ut else 'klar'))

if fel:
    print('\nAVBRYTER — html-bygget gick inte igenom.')
    for f in fel:
        print('  !', f)
    sys.exit(1)

browser = next((c for c in CHROME if os.path.exists(c)), None)
if not browser:
    print('\nHittar ingen webbläsare för PDF-utskrift. Skriv ut för hand med Ctrl+P.')
    sys.exit(1)

print('== pdf ==')
for html, pdf in PDF:
    src = os.path.join(ROOT, html)
    dst = os.path.join(ROOT, pdf)
    fore = os.path.getmtime(dst) if os.path.exists(dst) else 0
    subprocess.run([browser, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                    '--print-to-pdf=' + dst, 'file:///' + src.replace('\\', '/')],
                   capture_output=True)
    if not os.path.exists(dst) or os.path.getmtime(dst) <= fore:
        fel.append('%s skrevs inte om — gammal fil ligger kvar' % pdf)
        print('  %-22s MISSLYCKADES' % pdf)
        continue
    d = open(dst, 'rb').read()
    sidor = len(re.findall(rb'/Type\s*/Page[^s]', d))
    mb = len(d) / 1048576
    print('  %-22s %3d sidor  %5.2f MB' % (pdf, sidor, mb))
    if mb > 3:
        fel.append('%s är %.1f MB — för stor för att mejla' % (pdf, mb))
    if os.path.getmtime(dst) < os.path.getmtime(src):
        fel.append('%s är äldre än sin html' % pdf)

print('== kontroll ==')


def läs(f):
    return open(os.path.join(ROOT, f), encoding='utf-8').read()


ids = {}
for f in ['03-ovningsbank.html', '04-sasongsplan-host-2026.html', 'LAGPARMEN.html']:
    ids[f] = set(re.findall(r'id="ex-([A-Z0-9]+)"', läs(f)))
if len(set(map(frozenset, ids.values()))) != 1:
    fel.append('övnings-ID skiljer sig mellan filerna: ' +
               ', '.join('%s=%d' % (k, len(v)) for k, v in ids.items()))
else:
    print('  övnings-ID     %d, lika i alla filer' % len(next(iter(ids.values()))))

for f in ['03-ovningsbank.html', '04-sasongsplan-host-2026.html', 'LAGPARMEN.html',
          '09-positionsspel.html', '10-till-er-hemma.html']:
    h = läs(f)
    brutna = set(re.findall(r'href="#([a-zA-Z0-9-]+)"', h)) - set(re.findall(r'id="([a-zA-Z0-9-]+)"', h))
    if brutna:
        fel.append('%s har trasiga länkar: %s' % (f, sorted(brutna)))
    rester = (len(re.findall(r'\*\*', h)) + len(re.findall(r'^\|', h, re.M))
              + len(re.findall(r'@fig', h)) + len(re.findall(r'saknas\]', h)))
    if rester:
        fel.append('%s har %d rester av markdown eller saknade diagram' % (f, rester))
print('  länkar         kontrollerade')
print('  markdown       kontrollerad')

# Varje övningskod som nämns i lagmaterialet ska finnas i banken.
# CLAUDE.md räknas inte — den innehåller kodexempel med påhittade koder med flit.
bank = next(iter(ids.values()))
for f in glob.glob(os.path.join(ROOT, '*.md')):
    if os.path.basename(f) in ('CLAUDE.md',):
        continue
    txt = open(f, encoding='utf-8').read()
    nämnda = set(re.findall(r'\b((?:A|B|C|D|E|G|T|MV)\d{1,2})\b', txt))
    saknas = {k for k in nämnda if k not in bank} - {'A4', 'A3'}  # pappersformat, inte övningar
    if saknas:
        fel.append('%s hänvisar till koder som inte finns i banken: %s'
                   % (os.path.basename(f), sorted(saknas)))
print('  övningskoder   kontrollerade mot banken')

print()
if fel:
    print('!! %d PROBLEM' % len(fel))
    for f in fel:
        print('  !', f)
    sys.exit(1)
print('ALLT OK — de fyra PDF:erna är aktuella och går att skicka ut.')
