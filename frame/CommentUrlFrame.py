from javax.swing import JButton, JFrame, JPanel, JLabel, JTextArea, JTextField
from java.awt import Component, GridLayout, Frame


class CommentUrlFrame():

    def __init__(self, window_closing_handler):
        self.frame = JFrame("Add comments about this url",
            size = (300, 300)
        )

        self.frame.setLocationRelativeTo(self.getBurpFrame())
        self.windowClosing = window_closing_handler

        panel = JPanel(GridLayout(2,2))
        self.frame.add(panel)

        panel.add(JLabel("Select URL: "))
        panel.add(JTextField(""))

        panel.add(JTextArea(
            text = "TextArea",
            editable = True,
            wrapStyleWord = True,
            lineWrap = True,
            alignmentX = Component.LEFT_ALIGNMENT,
            size = (300, 1)
        ))

        self.frame.show()
    
    def getBurpFrame(self):
        for f in Frame.getFrames():
            if f.isVisible() and f.getTitle().find(("Burp Suite")) != -1:
                return f
        
        return None