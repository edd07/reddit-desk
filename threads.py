import threading
from PySide import QtGui, QtCore

import reddit

class requestSubmissionThread(QtCore.QThread):
    """ Retrieves a submission's comments without blocking the GUI thread"""    
    def __init__(self,submission):
        super(requestSubmissionThread,self).__init__()
        self.submission = submission
    def run(self):
        self.submission.comments
        
class requestPostListThread(QtCore.QThread):
    def __init__(self,postList,subreddit=None, reddit=None):
        super(requestPostListThread,self).__init__()
        self.subreddit = subreddit
        self.reddit = reddit
        self.postList = postList
        print "Spawning thread"
    def run(self):
        del self.postList[:] #Clears the list without losing the reference to the original
        if self.subreddit:
            list= self.subreddit.get_hot()
        elif self.reddit:        
            list=self.reddit.get_front_page()
        else:
            raise Exception("Wrong parameters")     
        for i in list:
            self.postList.append(i)

class loginThread(QtCore.QThread):
    """Logs a user in without blocking the GUI thread"""
    def __init__(self,reddit,user,password):
        self.reddit=reddit    
        self.user=user
        self.password=password
    def run(self):
        reddit.login(user=self.user,password=self.password)
                
        
            
    
        