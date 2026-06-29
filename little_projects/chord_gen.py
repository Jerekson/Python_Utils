from PIL import Image, ImageDraw, ImageFont
import math

# ── DATA ─────────────────────────────────────────────────────────────────────
# Each chord: (name, [strings top: E A D G B e], dots [(fret,string)], fingers_label, barre)
# strings: 'x' muted, 'o' open, '' not shown
# dots: (fret 1-4, string 0-5 where 0=low E, 5=high e)
# barre: (fret, from_string, to_string) or None

CHORDS = [
    # Row 1
    ("A",      ['x','o','','','','o'], [(2,1),(2,2),(2,3)],        "123\n(213)", None),
    ("A7",     ['x','o','','o','','o'], [(2,1),(2,3)],              "1  2\n(2  3)", None),
    ("Am",     ['x','o','','','','o'], [(2,1),(2,2),(1,3)],        "231",  None),
    ("Am7",    ['x','o','','','','o'], [(2,1),(1,3)],              "2  1",  None),
    ("Amaj7",  ['x','o','','','o',''], [(2,1),(1,2),(2,3)],        "213",  None),
    ("B♭",     ['x','','','','','x'], [(1,0),(2,1),(3,2),(3,3),(3,4)], "1234", None),

    # Row 2
    ("B7",     ['x','','o','','','o'], [(2,0),(1,1),(2,2),(3,3)],  "213 4", None),
    ("Bm",     ['x','','','','','x'], [(2,0),(3,1),(4,2),(2,3)],  "1342", None),
    ("C",      ['x','','o','','o','o'], [(3,0),(2,1),(1,2)],       "32 1",  None),
    ("C7",     ['x','','o','','','o'], [(3,0),(2,1),(4,2),(1,3)],  "3241", None),
    ("Cmaj7",  ['x','','o','o','o',''], [(3,0),(2,1)],             "32",   None),
    ("D",      ['x','x','o','','',''], [(1,2),(3,3),(2,4)],        "132",  None),

    # Row 3
    ("D7",     ['x','x','o','','',''], [(1,2),(2,3),(3,4)],        "213",  None),
    ("Dm",     ['x','x','o','','',''], [(2,2),(3,3),(1,4)],        "231",  None),
    ("Dm7",    ['x','x','o','','','o'], [(2,2),(1,3),(1,4)],       "211",  None),
    ("Dmaj7",  ['x','x','o','','',''], [(1,2),(2,3),(2,4)],        "123",  None),
    ("E",      ['o','','o','o','',''], [(2,0),(3,1),(1,2)],        "231",  None),
    ("E7",     ['o','','o','o','o','o'], [(2,0),(1,2)],            "2  1",  None),

    # Row 4
    ("Em",     ['o','','','o','o','o'], [(2,0),(3,1)],             "23",   None),
    ("Em7",    ['o','','o','o','o','o'], [(2,0)],                  "2",    None),
    ("F",      ['x','x','','','',''], [(3,0),(2,1),(1,2),(1,3)],   "3211", (1,1,5)),
    ("Fmaj7",  ['x','x','','','','o'], [(3,0),(2,1),(1,2)],        "321",  None),
    ("G",      ['','','o','o','o',''], [(2,0),(1,1),(3,4)],        "21  3", None),
    ("G7",     ['','','o','o','o',''], [(2,0),(1,1),(1,4)],        "32  1", None),
]

# ── LAYOUT ───────────────────────────────────────────────────────────────────
COLS = 6
ROWS = math.ceil(len(CHORDS) / COLS)

CELL_W = 160
CELL_H = 200
MARGIN = 40
PAGE_W = COLS * CELL_W + 2 * MARGIN
PAGE_H = ROWS * CELL_H + 2 * MARGIN + 40

# Chord grid dimensions
GRID_STRINGS = 6   # vertical lines
GRID_FRETS   = 5   # horizontal lines (4 fret spaces)
GW = 90            # grid pixel width
GH = 90            # grid pixel height
STRING_SPACING = GW / (GRID_STRINGS - 1)
FRET_SPACING   = GH / (GRID_FRETS - 1)
DOT_R = 7

BG    = (255, 255, 255)
INK   = (20,  20,  20)
GREY  = (120, 120, 120)

img = Image.new("RGB", (PAGE_W, PAGE_H), BG)
draw = ImageDraw.Draw(img)

# Try to load a decent font, fall back to default
try:
    font_name  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    font_finger= ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
except:
    font_name  = ImageFont.load_default()
    font_small = font_name
    font_finger= font_name
    font_title = font_name

# ── TITLE ────────────────────────────────────────────────────────────────────
draw.text((MARGIN, 10), "24 accords avec cordes à vide", font=font_title, fill=INK)

# ── DRAW EACH CHORD ──────────────────────────────────────────────────────────
def draw_chord(idx, chord):
    name, strings, dots, fingers, barre = chord
    col = idx % COLS
    row = idx // COLS

    # Top-left of the cell
    cx = MARGIN + col * CELL_W
    cy = MARGIN + 40 + row * CELL_H   # +40 for title

    # Grid top-left (centered in cell)
    gx = cx + (CELL_W - GW) // 2
    gy = cy + 40   # space for chord name + x/o markers

    # ── Chord name ──
    bbox = draw.textbbox((0, 0), name, font=font_name)
    tw = bbox[2] - bbox[0]
    draw.text((cx + (CELL_W - tw) // 2, cy + 2), name, font=font_name, fill=INK)

    # ── x / o markers ──
    for s, state in enumerate(strings):
        if state in ('x', 'o'):
            sx = gx + s * STRING_SPACING
            sy = gy - 14
            bbox2 = draw.textbbox((0, 0), state, font=font_small)
            sw = bbox2[2] - bbox2[0]
            draw.text((sx - sw // 2, sy - 8), state, font=font_small, fill=INK)

    # ── Barre ──
    if barre:
        bf, bs, be = barre
        x1 = gx + bs * STRING_SPACING
        x2 = gx + be * STRING_SPACING
        y  = gy + (bf - 1) * FRET_SPACING + FRET_SPACING / 2
        draw.line([(x1, y), (x2, y)], fill=INK, width=DOT_R * 2)

    # ── Grid lines ──
    for s in range(GRID_STRINGS):
        x = gx + s * STRING_SPACING
        draw.line([(x, gy), (x, gy + GH)], fill=INK, width=1)
    for f in range(GRID_FRETS):
        y = gy + f * FRET_SPACING
        lw = 3 if f == 0 else 1
        draw.line([(gx, y), (gx + GW, y)], fill=INK, width=lw)

    # ── Dots ──
    for fret, string in dots:
        dx = gx + string * STRING_SPACING
        dy = gy + (fret - 1) * FRET_SPACING + FRET_SPACING / 2
        draw.ellipse(
            [(dx - DOT_R, dy - DOT_R), (dx + DOT_R, dy + DOT_R)],
            fill=INK
        )

    # ── Finger numbers below ──
    bbox3 = draw.textbbox((0, 0), fingers, font=font_finger)
    fw = bbox3[2] - bbox3[0]
    fh = bbox3[3] - bbox3[1]
    draw.text(
        (cx + (CELL_W - fw) // 2, gy + GH + 6),
        fingers, font=font_finger, fill=INK, align="center"
    )

for i, chord in enumerate(CHORDS):
    draw_chord(i, chord)

out_path = "/mnt/user-data/outputs/accords_guitare.png"
img.save(out_path, dpi=(300, 300))
print(f"Saved: {out_path}  ({PAGE_W}×{PAGE_H}px)")
