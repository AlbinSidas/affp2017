"""SVG pitch-diagram generator for the Kopparspelet session plan."""

INK = "#10161C"
BLUE = "#1B3A6B"
COPPER = "#A85B2B"
VERD = "#3E7D6E"
FIELD = "#DDE5DF"
FIELDLINE = "#FFFFFF"
PAPER = "#E9ECE8"
GREY = "#8B948C"

W, H = 400, 300


def head(w=W, h=H):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" class="dgm">'
        '<defs>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
        f'markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M0,1 L9,5 L0,9 z" fill="{INK}"/></marker>'
        f'<marker id="arc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
        f'markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M0,1 L9,5 L0,9 z" fill="{COPPER}"/></marker>'
        f'<marker id="arb" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
        f'markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M0,1 L9,5 L0,9 z" fill="{BLUE}"/></marker>'
        '</defs>'
    )


def tail():
    return '</svg>'


def field(x, y, w, h, r=3):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{FIELD}" stroke="{FIELDLINE}" stroke-width="3"/>')


def dashbox(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="none" '
            f'stroke="{VERD}" stroke-width="2" stroke-dasharray="6 5"/>')


def line(x1, y1, x2, y2, col=FIELDLINE, wd=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{wd}"{d}/>')


def player(x, y, col=BLUE, label="", r=11):
    t = ''
    if label:
        t = (f'<text x="{x}" y="{y+4.5}" font-size="12" font-weight="700" '
             f'fill="#fff" text-anchor="middle" font-family="IBM Plex Mono, monospace">'
             f'{label}</text>')
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#fff" '
            f'stroke-width="2"/>{t}')


def ball(x, y, r=5):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{INK}" '
            f'stroke-width="2"/>')


def cone(x, y, s=7):
    return (f'<path d="M{x},{y-s} L{x+s*0.85},{y+s*0.6} L{x-s*0.85},{y+s*0.6} z" '
            f'fill="{COPPER}"/>')


def gate(x1, y1, x2, y2):
    return cone(x1, y1) + cone(x2, y2)


def goal(x, y, w=44, vertical=False, th=7):
    if vertical:
        return (f'<rect x="{x}" y="{y}" width="{th}" height="{w}" fill="{INK}" rx="2"/>')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{th}" fill="{INK}" rx="2"/>')


def run(x1, y1, x2, y2, col=INK, mk="ar"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="2.5" marker-end="url(#{mk})"/>')


def pas(x1, y1, x2, y2, col=BLUE, mk="arb"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#{mk})"/>')


def dribble(x1, y1, x2, y2, col=INK, amp=6, mk="ar"):
    """Wavy line = player travelling with the ball."""
    import math
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return ''
    ux, uy = dx / dist, dy / dist
    px, py = -uy, ux
    n = max(3, int(dist / 16))
    seg = (dist - 10) / n
    pts = [f'M{x1},{y1}']
    for i in range(n):
        a = 10 if i % 2 == 0 else -10
        mx = x1 + ux * (seg * (i + .5))
        my = y1 + uy * (seg * (i + .5))
        cx = mx + px * amp * (1 if i % 2 == 0 else -1)
        cy = my + py * amp * (1 if i % 2 == 0 else -1)
        ex = x1 + ux * (seg * (i + 1))
        ey = y1 + uy * (seg * (i + 1))
        pts.append(f'Q{cx:.1f},{cy:.1f} {ex:.1f},{ey:.1f}')
    return (f'<path d="{" ".join(pts)}" fill="none" stroke="{col}" '
            f'stroke-width="2.5" marker-end="url(#{mk})"/>')


def lbl(x, y, txt, size=11, col=INK, anchor="middle", weight=600):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" '
            f'text-anchor="{anchor}" font-weight="{weight}" '
            f'font-family="Source Sans 3, sans-serif">{txt}</text>')


def dim(x, y, txt):
    return (f'<text x="{x}" y="{y}" font-size="10.5" fill="{VERD}" '
            f'text-anchor="start" font-weight="700" letter-spacing="0.5" '
            f'font-family="IBM Plex Mono, monospace">{txt}</text>')
