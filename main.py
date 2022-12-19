from burp import IBurpExtender, IContextMenuFactory, IProxyListener
import controller.ContextMenuController as ContextMenuController
from java.io import PrintWriter
import json

import config.Config as Config
import service.url.PacketManager as PacketManager

class BurpExtender(IBurpExtender, IContextMenuFactory, IProxyListener):

    def registerExtenderCallbacks(self, callback):
        self.helper = callback.getHelpers()
        callback.setExtensionName("test")
        callback.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callback.getStdout(), True)
        callback.registerProxyListener(self.messageProxyListener)

        self.config = Config.Config()
        self.packet_manager = PacketManager.PacketManager(self.config)

        req_res = callback.getProxyHistory()
        self.packet_manager.init(req_res, self.helper)
        self.context_menu_controller = ContextMenuController.ContextMenuController(self.helper, self.config, self.packet_manager)

    def createMenuItems(self, invocation):
        return self.context_menu_controller.createContextMenu(invocation)
    
    def messageProxyListener(self, message_is_request, message):
        if message_is_request == True:
            self.context_menu_controller.setCommentFromNewMessage(message.getMessageInfo())