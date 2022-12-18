from burp import IBurpExtender, IContextMenuFactory
import controller.ContextMenuController as ContextMenuController
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callback):
        self.helper = callback.getHelpers()
        callback.setExtensionName("test")
        callback.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callback.getStdout(), True)

    def createMenuItems(self, invocation):
        context_menu = ContextMenuController.ContextMenuController(self.helper)

        return context_menu.createContextMenu(invocation)