# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Dec 23 15:24:58 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 552)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtGui.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboSubreddit = QtGui.QComboBox(self.layoutWidget)
        self.comboSubreddit.setMinimumSize(QtCore.QSize(200, 0))
        self.comboSubreddit.setMaxVisibleItems(20)
        self.comboSubreddit.setObjectName("comboSubreddit")
        self.verticalLayout.addWidget(self.comboSubreddit)
        self.listPosts = QtGui.QListWidget(self.layoutWidget)
        self.listPosts.setAlternatingRowColors(True)
        self.listPosts.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listPosts.setGridSize(QtCore.QSize(0, 100))
        self.listPosts.setWordWrap(False)
        self.listPosts.setObjectName("listPosts")
        self.verticalLayout.addWidget(self.listPosts)
        self.lineLogin = QtGui.QLineEdit(self.layoutWidget)
        self.lineLogin.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineLogin.setObjectName("lineLogin")
        self.verticalLayout.addWidget(self.lineLogin)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTitulo = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setText("")
        self.labelTitulo.setTextFormat(QtCore.Qt.PlainText)
        self.labelTitulo.setWordWrap(True)
        self.labelTitulo.setObjectName("labelTitulo")
        self.verticalLayout_2.addWidget(self.labelTitulo)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget1)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.webLink = QtWebKit.QWebView(self.tab_5)
        self.webLink.setUrl(QtCore.QUrl("about:blank"))
        self.webLink.setObjectName("webLink")
        self.horizontalLayout_6.addWidget(self.webLink)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.treeComentarios = QtGui.QTreeWidget(self.tab_6)
        self.treeComentarios.setAutoFillBackground(True)
        self.treeComentarios.setFrameShadow(QtGui.QFrame.Plain)
        self.treeComentarios.setAlternatingRowColors(True)
        self.treeComentarios.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeComentarios.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeComentarios.setIndentation(30)
        self.treeComentarios.setAnimated(True)
        self.treeComentarios.setAllColumnsShowFocus(True)
        self.treeComentarios.setWordWrap(True)
        self.treeComentarios.setHeaderHidden(True)
        self.treeComentarios.setObjectName("treeComentarios")
        self.treeComentarios.headerItem().setText(0, "1")
        self.horizontalLayout_7.addWidget(self.treeComentarios)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionUpvote = QtGui.QAction(MainWindow)
        self.actionUpvote.setCheckable(True)
        self.actionUpvote.setChecked(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/upvote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpvote.setIcon(icon)
        self.actionUpvote.setObjectName("actionUpvote")
        self.actionDownvote = QtGui.QAction(MainWindow)
        self.actionDownvote.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/downvote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownvote.setIcon(icon1)
        self.actionDownvote.setObjectName("actionDownvote")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Cliente reddit", None, QtGui.QApplication.UnicodeUTF8))
        self.lineLogin.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Login...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Link", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Comentarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpvote.setText(QtGui.QApplication.translate("MainWindow", "Upvote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpvote.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownvote.setText(QtGui.QApplication.translate("MainWindow", "Downvote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownvote.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
