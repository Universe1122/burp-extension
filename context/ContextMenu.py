from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JMenuItem

class ContextMenu(IBurpExtender, IContextMenuFactory):

    def __init__(self, parent_self):
        self.parent_self = parent_self
    
    def createContextMenu(self, parent_self, invocation):
        context = invocation.getInvocationContext()

        if context == IContextMenuInvocation.CONTEXT_MESSAGE_VIEWER_REQUEST or context == IContextMenuInvocation.CONTEXT_PROXY_HISTORY:
            menu_name = "Add comments about this url"
            menu_item = JMenuItem(menu_name, actionPerformed = self.test)
            menu_item.putClientProperty("test22", "aa")

            return [menu_item]

    def test(self, event):
        menu_item = event.getSource()
        get_data = menu_item.getClientProperty("test22")
        self.parent_self.stdout.println(get_data)