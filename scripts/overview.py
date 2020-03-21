from drawBot.drawBotDrawingTools import _drawBotDrawingTool
from fontTools.pens.cocoaPen import CocoaPen
from fontTools.ttLib import TTFont
from os import walk
from os.path import join


def drawGlyph(glyph):
	pen = CocoaPen(glyph._glyphset)
	glyph.draw(pen)
	path = pen.path
	_drawBotDrawingTool.drawPath(path)

_drawBotDrawingTool.drawGlyph = drawGlyph


s = 0.27
text_x = 130

def text_path(t, pos, font_path):
    # Like text, but draws paths of the glyphs
    x, y = pos
    f = TTFont(font_path)
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    save()
    translate(x, y)
    for char in t:
        glyph_name = cmap.get(ord(char), None)
        if glyph_name is not None:
            glyph = gs[glyph_name]
            drawGlyph(glyph)
            translate(glyph.width)
    restore()

def get_fonts_list():
    fonts = []
    for root, dirs, files in walk("../fonts"):
        for file_name in files:
            if file_name.endswith("ttf") and not file_name.startswith("."):
                font_path = join(root, file_name)
                f = TTFont(font_path)
                name = f["name"]
                family = name.getName(16, 3, 1,)
                if family is None:
                    family = name.getName(1, 3, 1).string.decode("utf-16_be")
                else:
                    family = family.string.decode("utf-16_be")
                style = name.getName(17, 3, 1)
                if style is None:
                    style = name.getName(2, 3, 1, 0x409).string.decode("utf-16_be")
                else:
                    style = style.string.decode("utf-16_be")
                fonts.append((
                    family,
                    f["OS/2"].usWidthClass,
                    f["OS/2"].usWeightClass,
                    -f["post"].italicAngle,
                    style,
                    font_path
                ))
                f.close()
    return sorted(fonts)
    
def overview(fonts_list):
    s = 0.1
    line_height = 1100
    size(1280, s * (line_height * len(fonts_list) + line_height * 0.3))
    
    # Move up
    save()
    translate(0, height())
    text_x = 300
    translate(0, -line_height * s * 0.9)
    for family, _, _, _, style, font_path in fonts_list:
        text("%s %s" % (family, style), (20, -26))
        translate(0, -line_height * s)
    restore()
    translate(0, height())
    scale(s)
    translate(0, -line_height)

    for family, _, _, _, style, font_path in fonts_list:
        translate(text_x)
        save()
        f = TTFont(font_path)
        upmscale = 1000.0 / f["head"].unitsPerEm
        scale(upmscale, upmscale)
        # print("%s %s" % (family, style))
        # stext_path("%s %s" % (family, style), (0, 0), font_path)
        text_path("Handgloves", (0, 0), font_path)
        restore()
        translate(-text_x, -line_height)

fonts = get_fonts_list()
overview(fonts)
saveImage("../images/overview.png")