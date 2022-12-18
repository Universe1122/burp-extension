from javax.swing import JButton, JFrame, JPanel, JLabel, JTextArea, JTextField, JPanel, BorderFactory
from java.awt import Component, GridLayout, Frame, GridBagLayout, GridBagConstraints, Dimension, Insets


class CommentUrlFrame():

    def __init__(self, window_closing_handler):
        self.frame = JFrame("Add comments about this url",
            size = (600, 300)
        )

        self.frame.setLocationRelativeTo(self.getBurpFrame())
        self.windowClosing = window_closing_handler

        panel = JPanel()
        gbl = GridBagLayout()
        panel.setLayout(gbl)
        panel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5))   # padding

        ################################
        # -> Create URL Info Layout
        #   -> Create Text Label
        gbc = GridBagConstraints()
        gbc.insets = Insets(0,0,5,5)    # padding
        gbc.gridx = 0
        gbc.gridy = 0
        gbc.weightx = 0.1
        gbc.fill = GridBagConstraints.BOTH
        panel.add(JLabel(" Select URL "), gbc)

        #   -> Create URL Text Field
        gbc = GridBagConstraints()
        gbc.insets = Insets(0,0,5,5)    # padding
        gbc.gridx = 1
        gbc.gridy = 0
        gbc.weightx = 0.9
        gbc.fill = GridBagConstraints.BOTH
        panel.add(JTextField(20), gbc)
        # -> End
        ################################

        ################################
        # -> Create Comment Info Layout
        #   -> Create Comment Label
        gbc = GridBagConstraints()
        gbc.gridx = 0
        gbc.gridy = 2
        gbc.fill = GridBagConstraints.BOTH
        panel.add(JLabel(" Enter Comments "), gbc)

        #   -> Create Comment TextArea Field
        gbc = GridBagConstraints()
        gbc.gridx = 1
        gbc.gridy = 2
        # gbc.gridwidth = 2
        # gbc.gridheight = 2
        gbc.weighty = 0.7
        gbc.fill = GridBagConstraints.BOTH
        panel.add(JTextArea(
            text = "TextArea",
            editable = True,
            wrapStyleWord = True,
            lineWrap = True,
            alignmentX = Component.LEFT_ALIGNMENT,
            size = (300, 40)
        ), gbc)
        # -> End
        ################################


        ################################
        # -> Create Button
        #   -> Create Cancel Button
        gbc = GridBagConstraints()
        gbc.gridx = 1
        gbc.gridy = 4
        gbc.insets = Insets(5,5,0,0)
        gbc.anchor = GridBagConstraints.WEST
        panel.add(JButton(" Cancel "), gbc)

        gbc = GridBagConstraints()
        gbc.gridx = 1
        gbc.gridy = 4
        gbc.insets = Insets(5,5,0,0)
        gbc.anchor = GridBagConstraints.EAST
        panel.add(JButton(" OK "), gbc)
        # -> End
        ################################

        self.frame.setContentPane(panel)
        self.frame.show()
    
    def getBurpFrame(self):
        for f in Frame.getFrames():
            if f.isVisible() and f.getTitle().find(("Burp Suite")) != -1:
                return f
        
        return None