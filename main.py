from burp import IBurpExtender, IContextMenuFactory
import controller.ContextMenuController as ContextMenuController
from java.io import PrintWriter
import json

import config.Config as Config
import service.url.PacketManager as PacketManager

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callback):
        self.helper = callback.getHelpers()
        callback.setExtensionName("test")
        callback.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callback.getStdout(), True)

        self.config = Config.Config()
        self.packet_manager = PacketManager.PacketManager()

    def createMenuItems(self, invocation):
        context_menu = ContextMenuController.ContextMenuController(self.helper, self.config, self.packet_manager)

        return context_menu.createContextMenu(invocation)