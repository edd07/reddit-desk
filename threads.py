import threading
from PySide import QtGui, QtCore

import reddit

class requestSubmissionThread(QtCore.QThread):    
    def __init__(self,submission):
        super(requestSubmissionThread,self).__init__()
        self.submission = submission
    def run(self):
        self.submission.comments
        

    
        