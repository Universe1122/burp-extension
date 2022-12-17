from javax.swing import JFrame, JButton
from java.awt import Frame

import frame.CommentUrlFrame as CommentUrlFrame

class CommentUrlPopup():

    def __init__(self):
        pass

    def onClickContextMenu(self, event):
        menuItem = event.getSource()
        get_data = menuItem.getClientProperty("test22")

        self.comment_url = CommentUrlFrame.CommentUrlFrame(self.onClose)

        # frame = JFrame("Add comments about this url",
        #     # defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
        #     size = (300, 300)
        # )
        # frame.setLocationRelativeTo(self.getBurpFrame())
        # frame.windowClosing = self.onClose

        # button = JButton(get_data)
        # frame.add(button)
        # frame.visible = True
    
    def onClose(self, event):
        pass