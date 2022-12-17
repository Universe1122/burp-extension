from burp import IBurpExtender, IContextMenuFactory
import context.ContextMenu as ContextMenu
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callback):
        self.helper = callback.getHelpers()
        callback.setExtensionName("test")
        callback.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callback.getStdout(), True)

    def createMenuItems(self, invocation):
        context_menu = ContextMenu.ContextMenu(self)

        return context_menu.createContextMenu(self, invocation)