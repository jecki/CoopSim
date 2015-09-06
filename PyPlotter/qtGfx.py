#!/usr/bin/python

# qtGfx -    Implementation of the Gfx.Driver Interface in a
#            qt evnironment

"""Implementes Gfx.Driver using the qt GUI toolkit.
"""

import sys, math
try:
    from PyQt5.Qt import Qt
    from PyQt5.QtCore import pyqtSignal as SIGNAL
    from PyQt5.QtCore import QPoint, QObject
    from PyQt5.QtWidgets import QApplication, QLabel
    import PyQt5.QtGui as qt
    QT3 = False
    QT5 = True
except ImportError:
    QT5 = False
    try:
        from PyQt4.Qt import Qt, SIGNAL
        from PyQt4.QtCore import QPoint, QObject
        import PyQt4.QtGui as qt
        from PyQt4.QtGui import QApplication, QLabel
        QT3 = False
    except ImportError: 
        import qt
        from qt import Qt, SIGNAL, QPoint, QObject, QApplication, QLabel
        QT3 = True
try:
    import Gfx
except ImportError:
    from . import Gfx

driverName = "qtGfx"


########################################################################
#
#   class Driver
#
########################################################################

class Driver(Gfx.Driver):
    """A graphics driver for qt4.
    For an explanation of the inherited methods see Gfx.py.
    """

    def __init__(self, paintDevice):
        """Initialize canvas on the QPaintDevice 'paintDevice'."""
        Gfx.Driver.__init__(self)
        self.paintDevice = None
        self.painter = qt.QPainter()        
        self.font = qt.QFont("SansSerif", 12, qt.QFont.Normal, False)
        self.pen = qt.QPen()
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.RoundJoin)
        self.brush = qt.QBrush(Qt.SolidPattern)
        self.color = (0.0, 0.0, 0.0)
        self.w, self. h = 640, 480        
        self.changePaintDevice(paintDevice)
        self.reset()
        self.clear()

    def changePaintDevice(self, paintDevice):
        """Use a new QPaintDevice for the following drawing commands."""
        oldPaintDevice = self.paintDevice
        if oldPaintDevice: 
            self.painter.end()
        self.paintDevice = paintDevice
        self.painter.begin(self.paintDevice)
        self.resizedGfx()
        self.painter.setPen(self.pen)
        self.painter.setBrush(Qt.NoBrush)
        self.painter.setBackgroundMode(Qt.TransparentMode)
        if QT3:
            self.painter.setBackgroundColor(qt.QColor(255,255,255))
        else:
            backgroundBrush = qt.QBrush(qt.QColor(255,255,255), Qt.SolidPattern)
            self.painter.setBackground(backgroundBrush)
        self.painter.setFont(self.font)
        return oldPaintDevice


    def getPaintDevice(self):
        """-> QPaintDevice of this graphics drivers object"""
        return self.paintDevice
    
    def _qtEnd(self):
        """Calls end() method of the QPainter obejct. Before any
        drawing can be done again qtBegin() must be called."""
        self.painter.end()

    def _qtBegin(self):
        """Calls begin() method of the QPainter obejct."""
        self.painter.begin()        


    def resizedGfx(self):
        self.w, self.h = self.paintDevice.width(), self.paintDevice.height()

    def getSize(self):
        return self.w, self.h

    def getResolution(self):
        return 100

    def setColor(self, rgbTuple):
        self.color = rgbTuple
        qtCol = qt.QColor(int(round(rgbTuple[0]*255)),
                          int(round(rgbTuple[1]*255)),
                          int(round(rgbTuple[2]*255)))
        self.pen.setColor(qtCol)
        self.brush.setColor(qtCol)
        self.painter.setPen(self.pen)

    def setLineWidth(self, width):
        self.lineWidth = width
        if width == Gfx.THIN: tn = 1
        elif width == Gfx.MEDIUM: tn = 2
        elif width == Gfx.THICK: tn = 3
        else: raise ValueError("'thickness' must be 'thin', 'medium' or thick' !")
        self.pen.setWidth(tn)
        self.painter.setPen(self.pen)

    def setLinePattern(self, pattern):
        self.linePattern = pattern
        if pattern == Gfx.CONTINUOUS: lp = Qt.SolidLine
        elif pattern == Gfx.DASHED: lp = Qt.DashLine
        elif pattern == Gfx.DOTTED: lp = Qt.DotLine
        else: raise ValueError("'pattern' must be 'continuous','dashed' " + \
                    "or 'dotted'")
        self.pen.setStyle(lp)
        self.painter.setPen(self.pen)

    def setFillPattern(self, pattern):
        self.fillPattern = pattern
        if pattern == Gfx.SOLID: fp = Qt.SolidPattern
        elif pattern == Gfx.PATTERN_A: fp = Qt.BDiagPattern
        elif pattern == Gfx.PATTERN_B: fp = Qt.FDiagPattern
        elif pattern == Gfx.PATTERN_C: fp = Qt.DiagCrossPattern
        else: raise ValueError("'pattern' must be 'solid' or 'patternA', " + \
                    "'patternB', 'patternC' !")
        self.brush.setStyle(fp)

    def setFont(self, ftype, size, weight):
        self.fontType = ftype
        self.fontSize = size
        self.fontWeight = weight
        if ftype == Gfx.SANS: ff = "SansSerif"
        elif ftype == Gfx.SERIF: ff = "Serif"
        elif ftype == Gfx.FIXED: ff = "Typewriter"
        else: raise ValueError("'type' must be 'sans', 'serif' or 'fixed' !")
        if size == Gfx.SMALL: fs = 8
        elif size == Gfx.NORMAL: fs = 12
        elif size == Gfx.LARGE: fs = 16
        else: raise ValueError("'size' must be 'small', 'normal' or 'large' !")
        fst = False
        fw = qt.QFont.Normal
        if "i" in weight: fst = True
        elif "b" in weight: fw = qt.QFont.Bold
        self.font = qt.QFont(ff, fs, fw, fst)
        self.painter.setFont(self.font)


    def getTextSize(self, text):
        fm = self.painter.fontMetrics()
        return fm.width(text), fm.height()
#        except AttributeError:
#           if self.fontSize == Gfx.SMALL: fs = 8
#            elif self.fontSize == Gfx.NORMAL: fs = 12
#            elif self.fontSize == Gfx.LARGE: fs = 16
#            return (len(text) * fs * 2/3, fs)   # very inexact

    def drawPoint(self, x, y):
        self.painter.drawPoint(x, self.h-y-1)
#        if self.lineWidth == Gfx.THIN:
#            self.dc.DrawPoint(x, self.h-y-1)
#        else:
#            self.dc.DrawLine(x, self.h-y-1, x, self.h-y-1)

    def drawLine(self, x1, y1, x2, y2):
        self.painter.drawLine(x1, self.h-y1-1, x2, self.h-y2-1)
        
    def drawRect(self, x, y, w, h):
        self.painter.drawRect(x, self.h-y-h, w-1 ,h-1)        

    def drawPoly(self, array):
        if array:
            points = [QPoint(p[0],self.h-p[1]-1) for p in array]
            if QT3:
                pointArray = qt.QPointArray(len(points))
                for i in range(len(points)):
                    pointArray.setPoint(i, points[i])
                self.painter.drawPolygon(pointArray)
            else:            
                self.painter.drawPolyline(qt.QPolygon(points))

    def drawCircle(self, x, y, r):
        self.painter.drawEllipse(x-r, self.h-y-1-r, 2*r, 2*r)


    def fillRect(self, x, y, w, h):
        self.painter.fillRect(x, self.h-y-h, w, h, self.brush)

    def fillPoly(self, array):
        if array:
            points = [QPoint(p[0],self.h-p[1]-1) for p in array]
            self.painter.setBrush(self.brush); self.painter.setPen(Qt.NoPen)
            if QT3:
                pointArray = qt.QPointArray(len(points))
                for i in range(len(points)):
                    pointArray.setPoint(i, points[i])
                self.painter.drawPolygon(pointArray)
            else:
                self.painter.drawPolygon(qt.QPolygon(points))
            self.painter.setPen(self.pen); self.painter.setBrush(Qt.NoBrush)

    def fillCircle(self, x, y, r):
        self.painter.setBrush(self.brush); self.painter.setPen(Qt.NoPen)
        self.painter.drawEllipse(x-r, self.h-y-1-r, 2*r, 2*r)        
        self.painter.setPen(self.pen); self.painter.setBrush(Qt.NoBrush)

    def writeStr(self, x, y, strg, rotationAngle=0.0):
        h = self.getTextSize(strg)[1]
        if rotationAngle == 0.0:
            self.painter.drawText(x, self.h-y-h/4, strg)
        else:
            rotationAngle = 360.0-rotationAngle
            cx = x
            cy = self.h-y
            self.painter.translate(cx, cy)
            self.painter.rotate(rotationAngle)
            self.painter.translate(-cx, -cy)
            self.painter.drawText(x, self.h-y-h/4, strg)
            if QT3:
                self.painter.resetXForm()                
            else:
                self.painter.resetTransform() 


########################################################################
#
#   class Window
#
########################################################################


class Window(Driver, Gfx.Window):
    
    def __init__(self, size=(640, 480), title="qt.Graph", app=None):
        Gfx.Window.__init__(self, size, title)
        if app != None:
            self.app = app
        else:
            self.app = QApplication(sys.argv)

        self.pixmap = qt.QPixmap(size[0], size[1])
        self.pixmap.fill(qt.QColor(255,255,255))
        self.win = QLabel("", None)
        self.win.setPixmap(self.pixmap)        
        self.win.show()                       
        #self.win.setMinimumSize(size[0], size[1])
        #self.win.setMaximum(size[0], size[1])
        self.win.resize(size[0], size[1])
        if QT5:
            #self.lastClosedSignal = SIGNAL("lastWindowClosed()")
            self.app.lastWindowClosed.connect(self._qtEnd)
        else:
            QObject.connect(self.app, SIGNAL("lastWindowClosed()"), self._qtEnd)
        Driver.__init__(self, self.pixmap) 

    def refresh(self):
        self.win.setPixmap(self.pixmap)         
        self.win.update()

    def quit(self):
        self._qtEnd()
        self.win.close()
        self.win = None
        self.app.quit()

    def waitUntilClosed(self):
        self.refresh()  
        if QT3:
            self.app.exec_loop()
        else:          
            self.app.exec_()



########################################################################
#
#   Test
#
########################################################################

if __name__ == "__main__":
    import systemTest
    systemTest.Test_qtGfx()
