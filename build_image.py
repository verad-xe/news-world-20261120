#!/usr/bin/env python3
"""Build entry.png: one editorial front-page image summing up the world news
of Friday 20 November 2026.

Layout (1024x1024): masthead with the date, a lead story with an original
generated illustration (assets/lead-kyiv.jpg, drawn for this entry, no text),
four news panels with short factual labels, and a footer ticker.
All text is set with PIL so every headline stays exact and legible.
Facts were checked against multiple reputable reports of 20 Nov 2026
(Reuters, AP, WSJ, CNN, Al Jazeera, NHK, Just Security, Investopedia).
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024

PAPER = (246, 241, 227)
PANEL = (255, 253, 246)
INK = (24, 34, 58)
NAVY = (18, 28, 54)
RED = (176, 44, 36)
GOLD = (198, 134, 22)
GREY = (84, 90, 102)
WHITE = (250, 248, 240)

SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=1.18):
    lines = wrap(draw, text, fnt, max_w)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def panel(draw, box, kicker, headline, body, accent):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL, outline=INK, width=3)
    draw.rectangle((x0, y0, x1, y0 + 10), fill=accent)
    draw.text((x0 + 18, y0 + 20), kicker, font=font(SANS_B, 20), fill=accent)
    y = text_block(draw, x0 + 18, y0 + 48, headline, font(SANS_B, 30), INK, x1 - x0 - 36, 1.12)
    text_block(draw, x0 + 18, y + 6, body, font(SANS_R, 21), (40, 44, 56), x1 - x0 - 36, 1.22)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead -------------------------------------------------------
    d.rectangle((0, 0, W, 8), fill=RED)
    d.text((28, 20), "THE WORLD IN ONE DAY", font=font(SERIF_B, 25), fill=INK)
    r = "AN ORIGINAL EDITORIAL SUMMARY"
    d.text((W - 28 - d.textlength(r, font=font(SANS_B, 16)), 27), r, font=font(SANS_B, 16), fill=GREY)
    date = "FRIDAY  20 NOVEMBER 2026"
    df = font(SANS_B, 57)
    d.text(((W - d.textlength(date, font=df)) / 2, 50), date, font=df, fill=NAVY)
    d.line((28, 122, W - 28, 122), fill=INK, width=3)
    d.line((28, 128, W - 28, 128), fill=INK, width=1)

    # ---- lead story -----------------------------------------------------
    lead = Image.open(os.path.join(HERE, "assets", "lead-kyiv.jpg")).convert("RGB")
    # crop a panoramic band (bridge + trails) and fit 968x212 at y=140
    band = lead.crop((0, 150, lead.width, int(lead.height * 0.92)))
    band = band.resize((968, 212))
    img.paste(band, (28, 140))
    d.rectangle((28, 140, 996, 352), outline=INK, width=3)
    tag = " LEAD STORY — UKRAINE WAR "
    tf = font(SANS_B, 20)
    tw = d.textlength(tag, font=tf)
    d.rectangle((28, 140, 28 + tw + 10, 172), fill=RED)
    d.text((33, 146), tag, font=tf, fill=WHITE)

    y = text_block(d, 28, 366, "RUSSIA HITS KYIV'S BRIDGES — MISSILES FALL IN POLAND",
                   font(SANS_B, 42), NAVY, 968, 1.1)
    text_block(d, 28, y + 4,
               "Overnight strikes kill 8 in Kyiv and injure 28 across nine regions. "
               "Two missiles and a drone cross into NATO member Poland — Warsaw calls "
               "it a deliberate provocation; allies condemn the violation.",
               font(SANS_R, 22), (40, 44, 56), 968, 1.22)

    # ---- four panels ----------------------------------------------------
    panel(d, (28, 548, 500, 768), "THE HAGUE — WORLD COURT",
          "MYANMAR COMMITTED GENOCIDE, ICJ RULES",
          "First time the World Court has held a state responsible for genocide: "
          "9–6 on the Rohingya. Reparations and safe return ordered. Myanmar rejects the verdict.",
          RED)
    panel(d, (524, 548, 996, 768), "BRUSSELS — EU–UK SUMMIT",
          "UK AND EU SIGN POST-BREXIT RESET DEAL",
          "Food trade, linked carbon markets and a youth mobility scheme — the "
          "biggest step back toward each other since Brexit.",
          GOLD)
    panel(d, (28, 784, 500, 956), "NEW YORK — MARKETS",
          "AI SELL-OFF SINKS WALL STREET",
          "S&P 500 −3.7%, into correction. Nasdaq −5.3%. Nvidia −14%, Nikkei −5%.",
          (30, 96, 140))
    panel(d, (524, 784, 996, 956), "PERU — EARTHQUAKE",
          "6.7 QUAKE SHAKES THE ANDES",
          "7:09 pm near Junín, felt in Lima. No casualties reported.",
          (36, 110, 84))

    # seismograph trace in the empty right end of the peru panel's kicker row
    pts2 = [(800, 814), (824, 814), (834, 802), (846, 826), (858, 806), (870, 820), (880, 814), (978, 814)]
    d.line(pts2, fill=RED, width=3)

    # ---- footer ticker --------------------------------------------------
    d.rectangle((0, 966, W, H), fill=NAVY)
    ticker = ("ALSO TODAY:  Saudi Arabia intercepts a Houthi missile and drones aimed at Riyadh  •  "
              "After the Shenzhen summit, Europe warns against a “new Yalta”  •  "
              "Los Angeles jury convicts the Palisades Fire arsonist")
    tf2 = font(SANS_B, 17)
    lines = wrap(d, ticker, tf2, 968)
    ty = 974
    for ln in lines[:2]:
        d.text((28, ty), ln, font=tf2, fill=WHITE)
        ty += 22

    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print(out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
