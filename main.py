# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Nov 28 13:26:41 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(747, 552)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Cliente reddit", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.splitter_2 = QtGui.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboSubreddit = QtGui.QComboBox(self.layoutWidget)
        self.comboSubreddit.setMinimumSize(QtCore.QSize(200, 0))
        self.comboSubreddit.setMaxVisibleItems(20)
        self.comboSubreddit.setObjectName(_fromUtf8("comboSubreddit"))
        self.comboSubreddit.addItem(_fromUtf8(""))
        self.comboSubreddit.setItemText(0, QtGui.QApplication.translate("MainWindow", "Front Page", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout.addWidget(self.comboSubreddit)
        self.listPosts = QtGui.QListWidget(self.layoutWidget)
        self.listPosts.setAlternatingRowColors(True)
        self.listPosts.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listPosts.setGridSize(QtCore.QSize(0, 100))
        self.listPosts.setWordWrap(False)
        self.listPosts.setObjectName(_fromUtf8("listPosts"))
        self.verticalLayout.addWidget(self.listPosts)
        self.lineLogin = QtGui.QLineEdit(self.layoutWidget)
        self.lineLogin.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineLogin.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Login...", None, QtGui.QApplication.UnicodeUTF8))
        self.lineLogin.setObjectName(_fromUtf8("lineLogin"))
        self.verticalLayout.addWidget(self.lineLogin)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelTitulo = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setText(_fromUtf8(""))
        self.labelTitulo.setTextFormat(QtCore.Qt.PlainText)
        self.labelTitulo.setWordWrap(True)
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.verticalLayout_2.addWidget(self.labelTitulo)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget1)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.webLink = QtWebKit.QWebView(self.tab_5)
        self.webLink.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webLink.setObjectName(_fromUtf8("webLink"))
        self.horizontalLayout_6.addWidget(self.webLink)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.treeComentarios = QtGui.QTreeWidget(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeComentarios.setFont(font)
        self.treeComentarios.setAlternatingRowColors(True)
        self.treeComentarios.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeComentarios.setIndentation(30)
        self.treeComentarios.setAnimated(True)
        self.treeComentarios.setAllColumnsShowFocus(True)
        self.treeComentarios.setWordWrap(True)
        self.treeComentarios.setHeaderHidden(True)
        self.treeComentarios.setObjectName(_fromUtf8("treeComentarios"))
        self.treeComentarios.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout_7.addWidget(self.treeComentarios)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.VoteToolbar = QtGui.QToolBar(MainWindow)
        self.VoteToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.VoteToolbar.setMovable(False)
        self.VoteToolbar.setFloatable(False)
        self.VoteToolbar.setObjectName(_fromUtf8("VoteToolbar"))
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.VoteToolbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.actionUpvote = QtGui.QAction(MainWindow)
        self.actionUpvote.setCheckable(True)
        self.actionUpvote.setChecked(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../.designer/backup/upvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpvote.setIcon(icon)
        self.actionUpvote.setText(QtGui.QApplication.translate("MainWindow", "Upvote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpvote.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpvote.setObjectName(_fromUtf8("actionUpvote"))
        self.actionDownvote = QtGui.QAction(MainWindow)
        self.actionDownvote.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../.designer/backup/downvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownvote.setIcon(icon1)
        self.actionDownvote.setText(QtGui.QApplication.translate("MainWindow", "Downvote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownvote.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownvote.setObjectName(_fromUtf8("actionDownvote"))
        self.VoteToolbar.addAction(self.actionUpvote)
        self.VoteToolbar.addAction(self.actionDownvote)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Link", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Comentarios", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
