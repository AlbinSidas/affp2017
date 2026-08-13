from diagrams import *
import json
D = json.load(open('svgs.json', encoding='utf-8'))
RED = "#C4302B"

# ---------- C5 : huvudet uppe ----------
s = head(400, 300)
s += field(25, 55, 350, 175)
s += dim(27, 45, "20 x 15 m · alla har boll · tränaren rör sig i ytan")
for x, y in [(80,100),(175,88),(280,110),(340,95),(70,180),(160,168),(255,190),(330,175)]:
    s += dribble(x, y, x+38, y-10, col=GREY, amp=5)
    s += player(x, y, BLUE)
    s += ball(x+13, y+11, 4)
s += player(200, 262, INK, r=12)
s += f'<text x="200" y="248" font-size="22" font-weight="700" fill="{COPPER}" text-anchor="middle" font-family="IBM Plex Mono, monospace">3</text>'
s += lbl(200, 290, "Tränaren håller upp fingrar — den som ser säger till", 11, INK)
s += f'<path d="M200,250 L200,236" stroke="{COPPER}" stroke-width="2.5" marker-end="url(#arc)"/>'
s += tail()
D['C5'] = s

# ---------- C6 : frågan före ----------
s = head(400, 320)
s += field(30, 50, 340, 180)
s += dim(32, 40, "3 mot 1 i ruta · frågan ställs FÖRE, inte efter")
s += player(90, 120, BLUE)
s += ball(105, 131, 4)
s += pas(108, 120, 215, 145, BLUE, "arb")
s += player(240, 150, BLUE)
s += player(310, 95, BLUE)
s += player(175, 185, COPPER)
s += f'<path d="M252,140 Q285,118 300,106" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ar)"/>'
s += f'<path d="M258,142 Q290,150 310,110" fill="none" stroke="{VERD}" stroke-width="2.5" marker-end="url(#ar)"/>'
s += f'<rect x="60" y="248" width="280" height="30" rx="4" fill="{COPPER}"/>'
s += f'<text x="200" y="268" font-size="13" font-weight="700" fill="#fff" text-anchor="middle" font-family="Oswald, sans-serif" letter-spacing="0.5">"VAR STÅR DEN FRIA?"</text>'
s += lbl(200, 296, "Frågan ställs innan passningen slås. Blicken följer en fråga —", 11, INK)
s += lbl(200, 313, "aldrig en tillsägelse. Titta upp betyder ingenting för ett barn.", 11, VERD)
s += tail()
D['C6'] = s

# ---------- OBS : observation protocol ----------
s = head(800, 340)
s += lbl(400, 28, "OBSERVATIONEN — TVÅ MINUTER, EN SPELARE", 16, INK, weight=700)
s += field(40, 52, 330, 190)
s += lbl(205, 236, "vanligt 3 mot 3", 10, VERD)
for x,y,c in [(110,130,BLUE),(185,105,BLUE),(150,190,BLUE),(255,120,COPPER),(300,175,COPPER),(215,200,COPPER)]:
    s += player(x,y,c,r=9)
s += f'<circle cx="185" cy="105" r="20" fill="none" stroke="{COPPER}" stroke-width="3"/>'
s += lbl(185, 76, "denna spelare", 10, COPPER)
s += player(120, 268, INK, r=11)
s += lbl(190, 272, "en tränare, ur coachrollen", 10, GREY, anchor="start", weight=500)
s += f'<rect x="440" y="62" width="320" height="168" rx="4" fill="{FIELD}" stroke="{FIELDLINE}" stroke-width="2.5"/>'
rows = [("MOTTAGNINGAR", "| | | |   | | | |   |", "11", INK),
        ("TITT FÖRE", "| | | |", "4", COPPER),
        ("FRAMÅT / SIDLED", "| | | |   | | |", "7", VERD)]
for i,(lab,marks,tot,col) in enumerate(rows):
    y = 96 + i*44
    s += lbl(462, y, lab, 10.5, col, anchor="start", weight=700)
    s += (f'<text x="462" y="{y+20}" font-size="15" fill="{INK}" font-family="IBM Plex Mono, monospace" '
          f'letter-spacing="1">{marks}</text>')
    s += (f'<text x="730" y="{y+16}" font-size="20" font-weight="700" fill="{col}" text-anchor="end" '
          f'font-family="IBM Plex Mono, monospace">{tot}</text>')
s += f'<line x1="452" y1="212" x2="748" y2="212" stroke="{FIELDLINE}" stroke-width="2"/>'
s += lbl(400, 304, "Vi säger ingenting under de två minuterna — annars mäter vi lydnad.", 12, RED)
s += lbl(400, 324, "4 av 11 = 36 % blick före mottagning. Siffran vi följer över tid.", 11, INK)
s += tail()
D['OBS'] = s

json.dump(D, open('svgs.json', 'w'))
print("diagrams:", len(D))
