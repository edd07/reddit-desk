import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ListItemDelegate(QItemDelegate):
    #linkActivated = Signal(str)
    #linkHovered = Signal(str)  # to connect to a QStatusBar.showMessage slot
    #upvoted = Signal()
    #downvoted = Signal()

    def __init__(self, parentView):
        QItemDelegate.__init__(self, parentView)
        assert isinstance(parentView, QAbstractItemView), \
            "The first argument must be the view"

        # We need that to receive mouse move events in editorEvent
        parentView.setMouseTracking(True)

        # Revert the mouse cursor when the mouse isn't over 
        # an item but still on the view widget
        parentView.viewportEntered.connect(parentView.unsetCursor)

        # documents[0] will contain the document for the last hovered item
        # documents[1] will be used to draw ordinary (not hovered) items
        self.documents = []
        for i in range(2):
            self.documents.append(QTextDocument(self))
            self.documents[i].setDocumentMargin(0)
        self.lastTextPos = QPoint(0,0)

    def drawDisplay(self, painter, option, rect, text): 
        # Because the state tells only if the mouse is over the row
        # we have to check if it is over the item too
        mouseOver = option.state & QStyle.State_MouseOver \
            and rect.contains(self.parent().viewport() \
                .mapFromGlobal(QCursor.pos())) \
            and option.state & QStyle.State_Enabled

        if mouseOver:
            # Use documents[0] and save the text position for editorEvent
            doc = self.documents[0]                
            self.lastTextPos = rect.topLeft()
            doc.setDefaultStyleSheet("")
        else:
            doc = self.documents[1]
            # Links are decorated by default, so disable it
            # when the mouse is not over the item
            doc.setDefaultStyleSheet("a {text-decoration: none}")

        doc.setDefaultFont(option.font)
        doc.setHtml(text)

        painter.save()
        painter.translate(rect.topLeft())
        ctx = QAbstractTextDocumentLayout.PaintContext()
        ctx.palette = option.palette
        doc.documentLayout().draw(painter, ctx)
        painter.restore()

    def editorEvent(self, event, model, option, index):
        if event.type() not in [QEvent.MouseMove, QEvent.MouseButtonRelease] \
            or not (option.state & QStyle.State_Enabled):
            return False                        
        # Get the link at the mouse position
        # (the explicit QPointF conversion is only needed for PyQt)
        pos = QPointF(event.pos() - self.lastTextPos)
        anchor = self.documents[0].documentLayout().anchorAt(pos)
        if anchor == "":
            self.parent().unsetCursor()
        else:
            self.parent().setCursor(Qt.PointingHandCursor)               
            if event.type() == QEvent.MouseButtonRelease:
                self.linkActivated.emit(anchor)
                return True 
            else:
                self.linkHovered.emit(anchor)
        return False

    def sizeHint(self, option, index):
        # The original size is calculated from the string with the html tags
        # so we need to subtract from it the difference between the width
        # of the text with and without the html tags
        size = QItemDelegate.sizeHint(self, option, index)

        # Use a QTextDocument to strip the tags
        doc = self.documents[1]
        html = index.data() # must add .toString() for PyQt "API 1"
        doc.setHtml(html)        
        plainText = doc.toPlainText()

        fontMetrics = QFontMetrics(option.font)                
        diff = fontMetrics.width(html) - fontMetrics.width(plainText)

        return size - QSize(diff, 0)
