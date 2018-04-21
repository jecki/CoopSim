# Transcrypt "hello world"


import Gfx
from canvasGfx import Driver


def testCanvas():
    canvas = document.getElementById('canvas')
    gfx = Driver(canvas)
    TestDriver(gfx)


def TestDriver(gfx):
    """Test Gfx.Interface. 'gfx' must be an object derived
    from a class that implements GfxDriver.GfxInterface."""

    w,h = gfx.getSize()
    if w < 400 or h < 300:
        raise "Graphics area too small: %d, %d !" % (w,h)

    gfx.clear()

    poly = [(10,20),(200, 10), (250, 100), (100, 180), (30, 40),(10,20)]

    gfx.setColor((0.7, 0.7, 0.5))
    gfx.setFillPattern(Gfx.PATTERNED)
    gfx.fillPoly(poly)

    gfx.setColor((1.0, 0.3, 0.3))
    gfx.setLinePattern(Gfx.DASHED)
    gfx.setLineWidth(Gfx.THIN)
    gfx.drawPoly(poly)

    gfx.setLinePattern(Gfx.DOTTED)
    gfx.setLineWidth(Gfx.THIN)
    gfx.drawRect(200, 200, 100, 100)

    gfx.setLineWidth(Gfx.THICK)
    gfx.setLinePattern(Gfx.DASHED)
    gfx.drawRect(300, 300, 120, 120)
    gfx.setLineWidth(Gfx.THIN)

    gfx.setLinePattern(Gfx.CONTINUOUS)
    gfx.setLineWidth(Gfx.MEDIUM)
    gfx.setFillPattern(Gfx.SOLID)
    gfx.setColor((0.3, 0.3, 0.3))
    gfx.fillRect(100,150,200,100)
    gfx.setColor((0.8, 0.0, 0.0))
    gfx.drawRect(150,150,210,110)
    gfx.setColor((0.1, 1.0, 0.1))
    gfx.setFont(Gfx.SANS, Gfx.NORMAL, "")
    gfx.writeStr(160,160, "Grafik")
    gfx.setFont(Gfx.SERIF, Gfx.LARGE, "bi")
    gfx.setColor((0.1, 1.0, 0.5))
    gfx.writeStr(170, 180, "Test")

    gfx.setFont(Gfx.SANS, Gfx.NORMAL, "")
    gfx.writeStr(100, 200, "wxGraph")
    gfx.writeStr(0, 0, "0")
    gfx.writeStr(90, 190, "Rotated", 90.0)
    gfx.setColor((0.5, 0.5, 0.5))
    gfx.drawLine(10, 10, 200, 100)
    for x in range(0, 361, 15):
        gfx.writeStr(500, 300, "Rotate " + str(x), float(x))
    gfx.setColor(Gfx.BLACK)
    gfx.writeStr(500, 100, "Rotation", 0.0)
    gfx.setColor(Gfx.RED)
    gfx.writeStr(500, 100, "Rotation", 90.0)
    gfx.setColor(Gfx.GREEN)
    gfx.writeStr(500, 100, "Rotation", 45.0)

    gfx.setLineWidth(Gfx.THIN)
    gfx.setColor(Gfx.BLUE)
    gfx.drawRect(350, 50, 100, 50)
    gfx.setColor(Gfx.GREEN)
    gfx.drawRect(349, 49, 102, 52)    
    gfx.setColor(Gfx.RED)
    gfx.fillRect(350, 50, 100, 50)
##    gfx.setColor(Gfx.GREEN)
##    gfx.drawRect(350, 50, 100, 50)
