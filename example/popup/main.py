## Reference https://gist.github.com/stefanocoding/d302f29a417a43b4f880e432b9ad1962

from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JMenuItem, JFrame, JButton
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Add Context Menu Example")
        callbacks.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        
    
    def createMenuItems(self, invocation):
        context = invocation.getInvocationContext()
        
        if context == IContextMenuInvocation.CONTEXT_MESSAGE_EDITOR_REQUEST or context == IContextMenuInvocation.CONTEXT_MESSAGE_VIEWER_REQUEST or context == IContextMenuInvocation.CONTEXT_PROXY_HISTORY:
            label = "test"
            menuItem = JMenuItem(label, actionPerformed = self.callFunction)
            menuItem.putClientProperty("test22", "aa")

            return [menuItem]
        
    
    def callFunction(self, event):
        menuItem = event.getSource()
        get_data = menuItem.getClientProperty("test22")
        self.stdout.println(get_data)

        frame = JFrame('Hello, Jython!',
            # defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (300, 300)
        )

        def change_text(event):
            self.stdout.println(get_data)

        button = JButton('Click Me!', actionPerformed=change_text)
        frame.add(button)
        frame.visible = True