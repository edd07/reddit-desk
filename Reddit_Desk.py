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
import sys
import datetime
from urllib2 import URLError
from PySide import QtGui, QtCore

import reddit

from ui import Ui_MainWindow
from item import Ui_Item
from itemComentario import Ui_ItemComentario


def unescape(string):
    if(string is not None):
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

class Reddit_Desk():
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QMainWindow()
    UI = Ui_MainWindow()
    reddit = reddit.Reddit(user_agent="reddit-desk")
    posts = []
    subredditList = []
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
                [self.UI.comboSubreddit.addItem(i.display_name) for i in self.subredditList]
                self.password=""
                self.UI.lineLogin.setText("")
                self.pasoLogin=0
                self.UI.lineLogin.setEchoMode(QtGui.QLineEdit.EchoMode(0))#login
            else:   
                self.UI.lineLogin.setEchoMode(QtGui.QLineEdit.EchoMode(0))#login
                self.UI.lineLogin.setText("Logged in as "+self.reddit.user.user_name)
                self.UI.lineLogin.setEnabled(False)
                self.refresh()
                
    
    def loadComment(self,comment, item):
        """
        Loads a comment widget with the comment's data and puts it onto the tree item       
        """
        commentItem = Ui_ItemComentario()
        widget = QtGui.QWidget()
        commentItem.setupUi(widget)
        commentItem.labelScore.setText(str(comment.ups - comment.downs)+" points")
        commentItem.labelComentario.setText(unescape(comment.body))
        commentItem.labelTime.setText(formatDate(comment.created))
        commentItem.labelRedditor.setText(comment.author.user_name)
        
        #commentItem.buttonUpvote.clicked.connect(comment.upvote)
        #commentItem.buttonDownvote.clicked.connect(comment.downvote)

        self.UI.treeComentarios.setItemWidget(item, 0 , widget)

    
    def loadReplies(self, comment, item):
        """
        Adds a comment's replies as children to that comment's tree item
        """
        for j in comment.replies:
            if type(j)!=type({}):                    
                child = QtGui.QTreeWidgetItem(item)
                item.addChild(child)
                self.loadComment(j, child)
                self.loadReplies(j,child)
    
    def loadSubreddit(self,current):
        """
        Fills the post list with the selected subreddit's font page
        """
        
        self.UI.listPosts.clear()
        if(self.UI.comboSubreddit.currentIndex() == 0):
            self.posts = self.reddit.get_front_page()
        elif(self.UI.comboSubreddit.currentIndex()<0):
            return
        else:
            self.posts = self.reddit.get_subreddit(
        self.subredditList[self.UI.comboSubreddit.currentIndex()-1].display_name).get_hot()
            
        for i in self.posts:
            item = QtGui.QListWidgetItem( self.UI.listPosts )
            subredditItem = Ui_Item()   
            widget = QtGui.QWidget()
            subredditItem.setupUi(widget)
            subredditItem.labelScore.setText(str(i.score))
            subredditItem.labelTitulo.setText(i.title)
            subredditItem.labelSubreddit.setText("in "+i.subreddit.display_name)
            subredditItem.labelRedditor.setText("by "+i.author.user_name)
            
            
            self.UI.listPosts.addItem(item)
            self.UI.listPosts.setItemWidget( item, widget)
            item.setSizeHint(QtCore.QSize(0,105))
        

    def loadSubmission(self):
        """
        Fills the title, web view and comment tree with the current submission
        """
        self.UI.labelTitulo.setText("Loading...")
                
        self.submission = self.posts[ self.UI.listPosts.currentRow() ]
        
         #webview
        if(self.submission.is_self):
            self.UI.webLink.setHtml(unescape(self.submission.selftext_html))
        else:
            self.UI.webLink.load(QtCore.QUrl(self.submission.url))
            
        
        #comments        
        self.UI.treeComentarios.clear()
        for i in self.submission.comments:
            if type(i)!=type({}): #The list has a dictionary at the end for some reason
                item = QtGui.QTreeWidgetItem(self.UI.treeComentarios)
                self.UI.treeComentarios.addTopLevelItem(item)
                self.loadComment(i,item)
                self.loadReplies(i,item)                

        
        self.UI.labelTitulo.setText(self.submission.title)
        
        self.UI.treeComentarios.expandAll()
    
    def __init__(self):
        self.UI.setupUi(self.form)
        
        #setup signals & slots:
        self.UI.listPosts.itemSelectionChanged.connect(self.loadSubmission)
        self.UI.comboSubreddit.currentIndexChanged.connect(self.loadSubreddit)     
        self.UI.lineLogin.returnPressed.connect(self.enterLogin)
        
        self.form.show()
        
        try:
            self.refresh()
        except URLError:
            self.UI.labelTitulo.setText("No Internet connection")
        
        sys.exit(self.app.exec_())
        
    def refresh(self):
        """
        Fills the Subreddit combobox and the post list with the user's front page
        """
        	
        self.UI.comboSubreddit.clear()
        
        if( self.reddit.user is not None ):
            self.subredditList = list(self.reddit.user.get_my_reddits())
        else:
            self.subredditList = [self.reddit.get_subreddit(i) for i in defaultSubreddits]
            
        self.UI.comboSubreddit.addItem("Front Page")
        [self.UI.comboSubreddit.addItem(i.display_name) for i in self.subredditList]
        
        self.loadSubreddit(0) #load the frontpage
        

if __name__ == "__main__":
    r = Reddit_Desk()