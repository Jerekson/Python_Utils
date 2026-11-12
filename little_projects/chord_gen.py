from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ══════════════════════════════════════════════════════════════════════════════
#  COLLECTIONS
#  Format d'un accord :
#  ( nom, [cordes E-A-D-G-B-e], [(fret, corde)], "doigts", barré )
#    - cordes : 'x' muette | 'o' à vide | '' rien
#    - dots   : fret 1-4, corde 0=Mi grave … 5=Mi aigu
#    - barré  : (fret, corde_début, corde_fin) ou None
# ══════════════════════════════════════════════════════════════════════════════

COLLECTIONS = [
    {
        "title": "24 accords à vide",
        "chords": [
            ("A",      ['x','o','','','','o'],   [(2,1),(2,2),(2,3)],          "123 (213)",   None),
            ("A7",     ['x','o','','o','','o'],   [(2,1),(2,3)],                "1 2 (2 3)",   None),
            ("Am",     ['x','o','','','','o'],   [(2,1),(2,2),(1,3)],          "231",          None),
            ("Am7",    ['x','o','','','','o'],   [(2,1),(1,3)],                "2 1",          None),
            ("Amaj7",  ['x','o','','','o',''],   [(2,1),(1,2),(2,3)],          "213",          None),
            ("Bb",     ['x','','','','','x'],    [(1,0),(2,1),(3,2),(3,3),(3,4)], "1234",      None),
            ("B7",     ['x','','o','','','o'],   [(2,0),(1,1),(2,2),(3,3)],    "213 4",        None),
            ("Bm",     ['x','','','','','x'],    [(2,0),(3,1),(4,2),(2,3)],    "1342",         None),
            ("C",      ['x','','o','','o','o'],  [(3,0),(2,1),(1,2)],          "32 1",         None),
            ("C7",     ['x','','o','','','o'],   [(3,0),(2,1),(4,2),(1,3)],    "3241",         None),
            ("Cmaj7",  ['x','','o','o','o',''],  [(3,0),(2,1)],                "32",           None),
            ("D",      ['x','x','o','','',''],   [(1,2),(3,3),(2,4)],          "132",          None),
            ("D7",     ['x','x','o','','',''],   [(1,2),(2,3),(3,4)],          "213",          None),
            ("Dm",     ['x','x','o','','',''],   [(2,2),(3,3),(1,4)],          "231",          None),
            ("Dm7",    ['x','x','o','','','o'],  [(2,2),(1,3),(1,4)],          "211",          None),
            ("Dmaj7",  ['x','x','o','','',''],   [(1,2),(2,3),(2,4)],          "123",          None),
            ("E",      ['o','','o','o','',''],   [(2,0),(3,1),(1,2)],          "231",          None),
            ("E7",     ['o','','o','o','o','o'], [(2,0),(1,2)],                "2 1",          None),
            ("Em",     ['o','','','o','o','o'],  [(2,0),(3,1)],                "23",           None),
            ("Em7",    ['o','','o','o','o','o'], [(2,0)],                      "2",            None),
            ("F",      ['x','x','','','',''],    [(3,0),(2,1),(1,2),(1,3)],    "3211",         (1,1,5)),
            ("Fmaj7",  ['x','x','','','','o'],   [(3,0),(2,1),(1,2)],          "321",          None),
            ("G",      ['','','o','o','o',''],   [(2,0),(1,1),(3,4)],          "21 3",         None),
            ("G7",     ['','','o','o','o',''],   [(2,0),(1,1),(1,4)],          "32 1",         None),
        ]
    },
    # ── Ajoute d'autres collections ici ──────────────────────────────────────
    # {
    #     "title": "Accords de La",
    #     "chords": [ ... ]
    # },
]

# ══════════════════════════════════════════════════════════════════════════════
#  SÉLECTION  — None = tout imprimer
# ══════════════════════════════════════════════════════════════════════════════

TO_PRINT = None   # ex: ["24 accords à vide"]

# ══════════════════════════════════════════════════════════════════════════════
#  LAYOUT  (toutes les mesures en mm, converties en points à l'usage)
# ══════════════════════════════════════════════════════════════════════════════

PAGE_W, PAGE_H = A4          # points  (595.27 x 841.89)
PAGE_W_MM = 210
PAGE_H_MM = 297

MARGIN_MM   = 10             # marge page
COLS        = 6              # accords par ligne
TITLE_MM    = 12             # hauteur du titre de collection

CELL_W_MM   = (PAGE_W_MM - 2*MARGIN_MM) / COLS
CELL_H_MM   = 38             # hauteur d'une cellule

GRID_W_MM   = CELL_W_MM * 0.70   # largeur de la grille
GRID_H_MM   = 18                  # hauteur de la grille (4 frettes)
STRING_N    = 6
FRET_N      = 5
SS          = GRID_W_MM / (STRING_N - 1)   # espacement entre cordes
FS          = GRID_H_MM / (FRET_N  - 1)   # espacement entre frettes
DOT_R_MM    = 1.4

# Typographie
FONT_TITLE  = 11   # pt
FONT_NAME   = 9    # pt
FONT_SMALL  = 6    # pt  (x / o)
FONT_FINGER = 5    # pt

INK = (0, 0, 0)

# ══════════════════════════════════════════════════════════════════════════════
#  ENREGISTREMENT DES FONTS
# ══════════════════════════════════════════════════════════════════════════════

def register_fonts():
    base = "/usr/share/fonts/truetype/dejavu/"
    try:
        pdfmetrics.registerFont(TTFont("DVSans",     base + "DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont("DVSansBold", base + "DejaVuSans-Bold.ttf"))
        return "DVSansBold", "DVSans"
    except:
        return "Helvetica-Bold", "Helvetica"

# ══════════════════════════════════════════════════════════════════════════════
#  DESSIN D'UN ACCORD  (coordonnées en mm, origine bas-gauche reportlab)
# ══════════════════════════════════════════════════════════════════════════════

def draw_chord(c, font_bold, font_reg, chord, cx_mm, cy_mm):
    """
    cx_mm, cy_mm = coin bas-gauche de la cellule (en mm).
    La cellule mesure CELL_W_MM x CELL_H_MM.
    """
    name, strings, dots, fingers, barre = chord

    # Grille centrée dans la cellule
    gx = cx_mm + (CELL_W_MM - GRID_W_MM) / 2   # x gauche de la grille
    # Disposition verticale dans la cellule (bas→haut) :
    #   fingers  : 3mm depuis le bas
    #   grille   : fingers_zone + GRID_H_MM
    #   x/o      : au-dessus de la grille
    #   nom      : tout en haut
    gy = cy_mm + 5           # bas de la grille
    top_grid = gy + GRID_H_MM

    # ── Nom de l'accord ──────────────────────────────────────────────────────
    c.setFont(font_bold, FONT_NAME)
    name_w = c.stringWidth(name, font_bold, FONT_NAME) / mm
    c.drawString((cx_mm + (CELL_W_MM - name_w)/2) * mm,
                 (top_grid + 5) * mm, name)

    # ── Marqueurs x / o ──────────────────────────────────────────────────────
    c.setFont(font_reg, FONT_SMALL)
    for s, state in enumerate(strings):
        if state in ('x', 'o'):
            sx = gx + s * SS
            sw = c.stringWidth(state, font_reg, FONT_SMALL) / mm
            c.drawString((sx - sw/2) * mm, (top_grid + 1.5) * mm, state)

    # ── Barré ─────────────────────────────────────────────────────────────────
    if barre:
        bf, bs, be = barre
        x1 = (gx + bs * SS) * mm
        x2 = (gx + be * SS) * mm
        y  = (gy + GRID_H_MM - (bf - 0.5) * FS) * mm
        c.setLineWidth(DOT_R_MM * 2 * mm)
        c.setLineCap(1)   # round
        c.line(x1, y, x2, y)
        c.setLineCap(0)

    # ── Lignes de grille ──────────────────────────────────────────────────────
    c.setLineWidth(0.3)
    for s in range(STRING_N):
        x = (gx + s * SS) * mm
        c.line(x, gy * mm, x, top_grid * mm)

    for f in range(FRET_N):
        y = (gy + f * FS) * mm
        c.setLineWidth(0.8 if f == FRET_N - 1 else 0.3)   # frette 0 (sillet) en haut
        c.line(gx * mm, y, (gx + GRID_W_MM) * mm, y)

    c.setLineWidth(0.3)

    # ── Points ───────────────────────────────────────────────────────────────
    c.setFillColorRGB(0, 0, 0)
    for fret, string in dots:
        dx = (gx + string * SS) * mm
        # fret 1 = espace entre frette 0 et frette 1 (en partant du haut)
        dy = (gy + GRID_H_MM - (fret - 0.5) * FS) * mm
        r  = DOT_R_MM * mm
        c.circle(dx, dy, r, stroke=0, fill=1)

    # ── Numéros de doigts ────────────────────────────────────────────────────
    c.setFont(font_reg, FONT_FINGER)
    fw = c.stringWidth(fingers, font_reg, FONT_FINGER) / mm
    c.drawString((cx_mm + (CELL_W_MM - fw)/2) * mm, (gy - 3.5) * mm, fingers)


# ══════════════════════════════════════════════════════════════════════════════
#  RENDU D'UNE COLLECTION (multi-pages si nécessaire)
# ══════════════════════════════════════════════════════════════════════════════

def render_collection(c, font_bold, font_reg, collection):
    chords = collection["chords"]
    title  = collection["title"]

    usable_h = PAGE_H_MM - 2*MARGIN_MM - TITLE_MM
    rows_per_page = int(usable_h // CELL_H_MM)

    idx      = 0
    page_num = 0

    while idx < len(chords):
        if page_num > 0:
            c.showPage()

        # Titre
        label = title if page_num == 0 else f"{title} (suite)"
        c.setFont(font_bold, FONT_TITLE)
        lw = c.stringWidth(label, font_bold, FONT_TITLE) / mm
        c.drawString(((PAGE_W_MM - lw) / 2) * mm,
                     (PAGE_H_MM - MARGIN_MM - TITLE_MM + 2) * mm, label)

        content_top = PAGE_H_MM - MARGIN_MM - TITLE_MM

        for row in range(rows_per_page):
            for col in range(COLS):
                if idx >= len(chords):
                    break
                cx = MARGIN_MM + col * CELL_W_MM
                # cy = bas de la cellule
                cy = content_top - (row + 1) * CELL_H_MM
                draw_chord(c, font_bold, font_reg, chords[idx], cx, cy)
                idx += 1

        page_num += 1


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    font_bold, font_reg = register_fonts()

    selected = COLLECTIONS if TO_PRINT is None else [
        col for col in COLLECTIONS if col["title"] in TO_PRINT
    ]

    out = "./accords_guitare.pdf"
    c = rl_canvas.Canvas(out, pagesize=A4)

    for i, collection in enumerate(selected):
        if i > 0:
            c.showPage()
        render_collection(c, font_bold, font_reg, collection)

    c.showPage()
    c.save()
    print(f"PDF sauvegardé : {out}")