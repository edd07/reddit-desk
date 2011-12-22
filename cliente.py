#===============================================================================
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
# 
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from item import Ui_Item
from itemComentario import Ui_ItemComentario
import reddit
import sys
import datetime
from urllib2 import URLError

def unescape(string):
    string = string.replace("&lt;", "<")
    string = string.replace("&gt;", ">")
    # this has to be last:
    string = string.replace("&amp;", "&")
    return string

def formatDate(num):
    return str(int(num/3600000)) + " hours ago"

defaultSubreddits = ["pics","gaming","worldnews","videos","todayilearned", \
    "IAmA","funny","atheism", "politics","science","AskReddit","technology", \
    "WTF","blog","announcements","bestof","AdviceAnimals","Music","aww", \
    "askscience","movies"]

class Cliente():
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QMainWindow()
    UI = Ui_MainWindow()
    reddit = reddit.Reddit(user_agent="reddit-desk")
    posts = []
    listaSubreddits = []
    comments = []
    loggedIn = False
    username =""
    password =""
    pasoLogin=0
    
    def enterLogin(self):
        if(self.pasoLogin==0):
            self.username = str(self.UI.lineLogin.text())
            
            self.UI.lineLogin.setText("")
            self.UI.lineLogin.setEchoMode(QtGui.QLineEdit.EchoMode(2)) #password
            self.pasoLogin=1
        elif(self.pasoLogin==1):
            self.password = str(self.UI.lineLogin.text())
            
            try:
                self.reddit.login(self.username, self.password)
            except reddit.api_exceptions.InvalidUserPass:
                [self.UI.comboSubreddit.addItem(i.display_name) for i in self.listaSubreddits]
                self.password=""
                self.UI.lineLogin.setText("")
                self.pasoLogin=0
                self.UI.lineLogin.setEchoMode(QtGui.QLineEdit.EchoMode(0))#login
            else:   
                self.UI.lineLogin.setEchoMode(QtGui.QLineEdit.EchoMode(0))#login
                self.UI.lineLogin.setText("Logged in as "+self.reddit.user.user_name)
                self.UI.lineLogin.setEnabled(False)
                self.refresh()
                
    
    def cargarComentario(self,comment, item):
        """
        Toma un comentario y llena el widget con la informacion
        
        """
        
        commentItem = Ui_ItemComentario()
        widget = QtGui.QWidget()
        commentItem.setupUi(widget)
        commentItem.labelScore.setText(str(comment.ups - comment.downs)+" points")
        commentItem.labelComentario.setText(unescape(comment.body))
        commentItem.labelTime.setText(formatDate(comment.created))
        commentItem.labelRedditor.setText(comment.author.user_name)
        
        commentItem.buttonUpvote.clicked.connect(comment.upvote)
        commentItem.buttonDownvote.clicked.connect(comment.downvote)

        self.UI.treeComentarios.setItemWidget( item,0, widget) #buscar el ItemDelegate

    
    def cargarReplies(self, comment, item):
        """
        Toma un comentario y un item para el, agrega todas las replies
        y las pone como hijos del item
        """
        
        for j in comment.replies:
                    if type(j)!=type({}):                    
                        child = QtGui.QTreeWidgetItem(item)
                        item.addChild(child)
                        self.cargarComentario(j, child)
                        self.cargarReplies(j,child)
    
    def cargarSubreddit(self,current):
        """
        Llena la lista de posts con la frontpage del subreddit seleccionado
        en el combo box
        """
        
        self.UI.listPosts.clear()
        if(current == 0):
            self.posts = self.reddit.get_front_page()
        elif(current<0):
            return
        else:
            self.posts = self.reddit.get_subreddit(self.listaSubreddits[current-1].display_name).get_hot()
            
        for i in self.posts:
            item = QtGui.QListWidgetItem( self.UI.listPosts )
            subredditItem = Ui_Item()   
            widget = QtGui.QWidget()
            subredditItem.setupUi(widget)
            subredditItem.labelScore.setText(str(i.score))
            subredditItem.labelTitulo.setText(i.title)
            subredditItem.labelSubreddit.setText("in "+i.subreddit.display_name)
            subredditItem.labelRedditor.setText("by "+i.author.user_name)
            
            self.UI.listPosts.setItemWidget( item, widget) #debe hacerse mejor con el ItemDelegate
            self.UI.listPosts.addItem(item)
            item.setSizeHint(QtCore.QSize(0,105))
        

    def cargarSubmission(self):
        """
        Llena el titulo, el webView y los comentarios con la submission seleccionada en la lista
        """
        self.submission = self.posts[ self.UI.listPosts.currentRow() ]
        
        self.UI.labelTitulo.setText(self.submission.title) #titulo
        
         #llenar webview
        self.UI.webLink.setHtml("Loading...")
        if(self.submission.is_self):
            self.UI.webLink.setHtml( unescape( self.submission.selftext_html ) )
        else:
            self.UI.webLink.load( QtCore.QUrl( self.submission.url ) )
            
        #comentarios
        self.UI.treeComentarios.clear()
        for i in self.submission.comments:
            if type(i)!=type({}): #si no es un diccionario
                item = QtGui.QTreeWidgetItem(self.UI.treeComentarios)
                self.UI.treeComentarios.addTopLevelItem(item)
                self.cargarReplies(i,item)                
                self.cargarComentario(i,item)

        self.UI.treeComentarios.expandAll()
    
    def __init__(self):
        #setup GUI
        self.UI.setupUi(self.form)
        self.form.show()
        
        #setup signals & slots:
        #QtCore.QObject.connect(self.UI.listPosts, QtCore.SIGNAL("itemSelectionChanged()"), self.cargarSubmission)
        self.UI.listPosts.itemSelectionChanged.connect(self.cargarSubmission)
        self.UI.comboSubreddit.currentIndexChanged.connect(self.cargarSubreddit)     
        self.UI.lineLogin.returnPressed.connect(self.enterLogin)
        
        try:
            self.refresh()
        except URLError:
            self.UI.labelTitulo.setText("No hay conexion a internet")
        
        sys.exit(self.app.exec_())
        
    def refresh(self):
        	
        #Llena el combo de subreddits, y carga la lista con la frontpage
        
        # cargar combobox de subreddits
        self.UI.comboSubreddit.clear()
        
        if( self.reddit.user is not None ):
            self.listaSubreddits = list(self.reddit.user.get_my_reddits())
        else:
            self.listaSubreddits = [self.reddit.get_subreddit(i) for i in defaultSubreddits]
            
        self.UI.comboSubreddit.addItem("Front Page")
        [self.UI.comboSubreddit.addItem(i.display_name) for i in self.listaSubreddits]
        self.cargarSubreddit(0) #cargar la frontpage
        

if __name__ == "__main__":
    r = Cliente()