from javax.swing import JFrame, JButton
from java.awt import Frame

import ui.CommentUrlFrame as CommentUrlFrame
import config.Config as Config
import service.url.PacketManager as PacketManager

class CommentUrlPopupService():

    def __init__(self, config, packet_manager):
        self.config = config
        self.packet_manager = packet_manager

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

        # Get data from user input
        input_url = self.form.input_url.getText()
        comment = self.form.input_comment.getText()

        self.setComment(input_url, comment)
    
    def setComment(self, url, comment):

        # Set comment in burp message
        self.set_comment_func(comment)

        # Close this popup
        self.form.frame.dispose()

        # Save comment of url
        self.packet_manager.setPacketInfo(url, {"comment" : comment})
        
        # Save data to file
        self.config.savePacketInfo(self.packet_manager.getPacketInfoAll())