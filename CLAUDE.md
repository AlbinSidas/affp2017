# CLAUDE.md

Context for Claude Code working in this repository.

## What this is

Training material for **one youth team** — P9 (born 2017) at Åtvidabergs FF, a Swedish club. Written for the team's three volunteer coaches. Scope is deliberately one team, not the club; club-level material is parked in `_parkerat/` and should stay there unless explicitly asked for.

**Working language is Swedish.** Write in Swedish unless a file is explicitly marked `-EN`. Those three files are background source material and stay in English.

## Architecture

The repo root **is** the published site (GitHub Pages serves from root). Flat, eight
working documents plus the compiled distribution files:

```
01-sa-spelar-vi.md            playing idea — BOLL · MOD · PRESS
02-sa-tranar-vi.md            purpose of training, session structure, staffing, scanning
03-ovningsbank.html           31 exercises            [generated]
04-sasongsplan-host-2026.html 26 sessions             [generated]
05-matning-och-utveckling.md  testing and observation
06-spelarna-och-vuxna.md      differentiation, behaviour, own child, food, boundaries
07-matguide.html              nutrition infographics  [generated]
08-arshjul.md                 training periods, theme blocks, activities, deadlines
LAGPARMEN.html                everything above in one print/PDF file  [generated]
index.html                    landing page for GitHub Pages           [generated]
*.pdf                         four distribution PDFs                  [generated]
MALL-sasongsplan.md           template for next season
README.md · LICENSE           public-facing; CC BY-SA 4.0
_bygg/                        build scripts
_parkerat/                    parked club-level material — do not expand
_internt/                     working documents — gitignored, never published
```

**This repo is public.** Three rules follow from that, and they outrank convenience:

1. **No individual player names anywhere** — not even as examples in coaching dialogue.
   Use `[namn]`. Same for guardians, addresses, phone numbers and e-mail.

   **One deliberate exception:** the author attribution and ÅFF disclaimer names
   *Albin Sidås* and gives *albinsidas@gmail.com*. It appears in `README.md`, `LICENSE`,
   `LASMIG.md`, `index.html` and the footer of every generated document. It exists so
   nobody can read the material as an official club position, and so questions have
   somewhere to go. **Do not strip it, and do not spread it further** — the coaching text
   itself stays role-based (`huvudtränaren`, never a name), because a document written to
   one named person dies with that person.
2. **Nothing written to ourselves goes in the root.** Internal deliberation, review
   findings and work plans live in `_internt/`, which is gitignored.
3. **Other clubs may fork this.** Prefer wording that generalises — a team can change
   dates, game format and squad size without rewriting the argument.

**Distribution model: two files, not nine.** Coaches get `LAGPARMEN.html` (print → one PDF).
Guardians get `07-matguide.html`. Everything else is source.

**Read `LASMIG.md` first.** It is the map and states the rules.

## The governing principle

> The season plan references the exercise bank by ID. It never copies exercise text.

Improve exercise `A3` in the bank and the season plan improves with it. This is what keeps three coaches saying the same things.

## Generated files — do not hand-edit

Four files are build output:

| File | Built by |
|---|---|
| `03-ovningsbank.html` | `_bygg/bank.py` |
| `07-matguide.html` | `_bygg/matguide.py` |
| `04-sasongsplan-host-2026.html` | `_bygg/build.py` |
| `LAGPARMEN.html` | `_bygg/parm.py` |

**Always run the whole chain, never the scripts one at a time:**

```bash
cd _bygg
python bygg-allt.py
```

It builds every HTML file, renders all four PDFs, and then verifies: exercise-ID parity
across files, no broken `#` anchors, no leftover markdown, no missing diagrams, no
references to exercise codes that do not exist, no PDF over 3 MB, and no PDF older than
its HTML. It exits with **ALLT OK** or a list of problems.

That last check exists because hand-run PDF steps failed silently twice and left stale
PDFs that looked finished. Do not go back to running the steps individually.

| Script | Writes |
|---|---|
| `build.py` | `04-sasongsplan-host-2026.html` — owns `EX` (exercises) and `S` (sessions) |
| `bank.py` | `03-ovningsbank.html` |
| `matguide.py` | `07-matguide.html` |
| `parm.py` | `LAGPARMEN.html` |
| `doc.py` | `09-positionsspel.html`, `10-till-er-hemma.html` |
| `index.py` | `index.html` |
| `md.py` | shared markdown→HTML converter and page shell — no output of its own |
| `nya_svgs.py` | diagrams into `svgs.json` and `pos_svgs.json`; run only when diagrams change |

The two distribution PDFs are rendered from the HTML with headless Chrome — no extra
dependency, and it honours the `@media print` rules:

```bash
chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=Lagparmen.pdf LAGPARMEN.html
chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=Matguide.pdf 07-matguide.html
```

Roughly 81 A4 pages / 1.5 MB and 8 pages / 250 kB. Anything that pushes the lagpärm past
~3 MB should be treated as a regression — it has to survive being emailed.

`parm.py` runs last — it reads the Markdown files and the `EX`/`S` data from `build.py`.
Edit a Markdown file, rerun `parm.py`, and the PDF edition follows. It contains its own
minimal Markdown converter; the sources only use headings, tables, lists, blockquotes,
`---`, `**bold**`, `*italic*` and backtick code.

Requires Python 3 only. Optional, for previewing diagrams as PNG: `pip install cairosvg`.

**Editing exercises or sessions means editing `_bygg/build.py`, then rebuilding both.** `bank.py` reads its exercise data from `build.py`, so the two HTML files can never disagree.

### Where things live in build.py

- `EX` — list of exercise tuples: `(code, name, category, area, time, setup, howto, [coaching points], differentiation)`
- `S` — list of 26 session dicts, built by the `tue()` / `thu()` helpers
- `css` — the stylesheet, shared with `bank.py`
- The HTML template is at the bottom

### Diagrams

`_bygg/svgs.json` holds every diagram as an SVG string, keyed by exercise code. `_bygg/diagrams.py` is the drawing library — `player()`, `ball()`, `cone()`, `goal()`, `run()`, `pas()`, `dribble()`, `field()`, `lbl()`, `dim()`.

To add or replace a diagram, write a short script that loads the JSON, sets a key, dumps it:

```python
from diagrams import *
import json
D = json.load(open('svgs.json', encoding='utf-8'))
s = head(400, 300)
s += field(30, 40, 340, 200)
s += player(200, 140, BLUE)
s += tail()
D['A6'] = s
json.dump(D, open('svgs.json', 'w'))
```

Symbol conventions are binding — see `_bygg/symboler-och-id.md`. Blue = attacker, copper = defender, green = goalkeeper, wavy arrow = travelling with the ball, dashed = pass, solid = run without the ball.

**Check text fits the viewBox.** Long label strings overflow silently; render to PNG and look before committing.

## ID rules — these are load-bearing

1. An ID means the same thing forever. `A3` is Grindar across the whole club, in every age group, in every year.
2. An ID is never reused. If an exercise is removed the number is retired, so old season plans stay readable.
3. Improvements rewrite the existing entry. The code never changes, so every team inherits the improvement.

Prefixes: `A` running with the ball · `B` 1v1 · `C` first touch and scanning · `D` passing and support · `E` pressing and defending · `MV` goalkeeping · `T` tests · `G` game formats · `ANK`/`KAR`/`TRK` structure.

`D1`–`D6` and `E1`–`E4` were added in August 2026 to close the two real holes in the bank: there was no passing/receiving/combination exercise at all, and nothing for PRESS despite it being one of the three words in the playing idea. They are documented in full in `09-positionsspel.md` ch. 8 — keep the two in sync.

## Editorial rules

- **No individual player names, assessments, or levels** in any shared document.
- **No test results tied to names.** Results belong to the player, on the player's own card.
- **Nothing written to one named coach.** A document written to one person dies with that person. Write so the next coach can use it.
- Age-appropriateness is binding. The "what we deliberately do NOT do" column in `02-sa-tranar-vi.md` carries the same weight as the left column.
- **Development is the stated purpose of training.** Do not soften `02-sa-tranar-vi.md` §"Vad träningen är till för" back into participation-for-its-own-sake language. Demands are on engagement and effort at training, never on selection, ranking, or match minutes — those are fixed by §5 of `06-spelarna-och-vuxna.md`.
- **Passvärd is the head coach, every session, and does not rotate.** Name the role, never the person.
- The commitments in `06-spelarna-och-vuxna.md` §5 constrain everything else. If a change conflicts with them, the change is wrong.
- **Scope discipline.** This is one team's material. Do not reintroduce club-wide structures, roles, or coordination mechanisms — that scope was deliberately retired.

### Nutrition content — handle with care

`06-spelarna-och-vuxna.md` and `07-matguide.html` concern children aged 8–12.

- **No gram, calorie, or macro targets.** Ever. Guidance is about adequacy and timing only.
- **No supplements, sports drinks, protein powder, or carbohydrate loading.** Most published sports-nutrition advice targets teenagers or adult elite athletes and must not be scaled down to children.
- **Never frame food as good/bad, never as reward or punishment, never comment on weight or body shape.** These rules are in `06-spelarna-och-vuxna.md` and outrank any performance consideration.
- Underfuelling is the real risk at this age, not overeating. Keep the emphasis there.
- If a change would make the material read as performance nutrition for children, the change is wrong.

## After any change

Verify before considering the work done:

- Exercise IDs identical in both HTML files
- No broken `href="#..."` anchors
- Every filename referenced in prose actually resolves
- No stale exercise names left in session descriptions — these are free text and do **not** update automatically when an exercise is renamed. This has broken twice.

```bash
cd _bygg && python3 - <<'EOF'
import re, pathlib
b=set(re.findall(r'id="ex-([A-Z0-9]+)"',open('../03-ovningsbank.html',encoding='utf-8').read()))
p=set(re.findall(r'id="ex-([A-Z0-9]+)"',open('../04-sasongsplan-host-2026.html',encoding='utf-8').read()))
print("parity:", b==p, len(b))
for f in ['../03-ovningsbank.html','../04-sasongsplan-host-2026.html']:
    h=open(f,encoding='utf-8').read()
    ids=set(re.findall(r'id="([a-zA-Z0-9-]+)"',h)); lk=set(re.findall(r'href="#([a-zA-Z0-9-]+)"',h))
    print(f.split('/')[-1], "broken:", lk-ids or "none")
EOF
```

## Adding a new season

Copy `MALL-sasongsplan.md`. Three or four blocks of 3–4 weeks, exercises referenced from the bank by ID, three test days roughly five weeks apart. The last week of each block is a bridge week: new theme in the station, old theme still a condition in the games.

## Measurement — the important part

`05-matning-och-utveckling.md` distinguishes three levels of evidence: can do it in a test (weak), does it when told (compliance), does it when nobody speaks (learning). Only the third counts.

Two in-game observations matter more than the technical card: **O1 scans before receiving** and **O2 first action forward**. They are counted live over two minutes per player, in silence. O1 is the metric to preserve above all others — it works identically at nine and nineteen.

Never let test results become ranking, selection, or team allocation.

## Context worth knowing

Eighteen boys, three coaches. Tuesday 90 min on the 7v7 pitch, Thursday 60 min on the 5v5 pitch with about thirteen present. Spelform is 5 mot 5 this season, 7 mot 7 next year. Goalkeepers rotate; several boys want to play there.

The group's clearest weakness is scanning — lifting the eyes off the ball. That is the season's priority, but it is downstream of first touch: a player whose touch is unreliable *must* look down. Fix the touch and part of the scanning follows.

Development is the stated purpose of training: a session that developed nobody is a failed session, however much fun it was. Retention still matters and is still counted (March vs October), but it is treated as an *outcome* of training worth returning to — never as a reason to lower demands. Children quit from aimless, chaotic sessions as readily as from hard ones.
