from javax.swing import JFrame, JButton
from java.awt import Frame

import ui.CommentUrlFrame as CommentUrlFrame

class CommentUrlPopupService():

    def __init__(self):
        pass

    def onClickContextMenu(self, event):
        menuItem = event.getSource()
        data = {
            "request_url" : menuItem.getClientProperty("request_url"),
            "comment" : menuItem.getClientProperty("comment")
        }
        self.set_comment_func = menuItem.getClientProperty("set_comment_func")

        self.form = CommentUrlFrame.CommentUrlFrame(self.onClose, self.closeBtnClick, self.okBtnClick, data)
    
    def onClose(self, event):
        self.form.frame.dispose()

    def closeBtnClick(self, event):
        self.form.frame.dispose()

    def okBtnClick(self, event):
        input_url = self.form.input_url.getText()
        comment = self.form.input_comment.getText()

        self.set_comment_func(comment)
        self.form.frame.dispose()