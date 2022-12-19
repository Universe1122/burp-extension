from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JMenuItem

import service.CommentUrlPopupService as CommentUrlPopupService

class ContextMenuController(IBurpExtender, IContextMenuFactory):

    def __init__(self, helper, config, packet_manager):
        self.helper = helper
        self.config = config
        self.packet_manager = packet_manager
    
    def createContextMenu(self, invocation):
        context = invocation.getInvocationContext()

        if context == IContextMenuInvocation.CONTEXT_MESSAGE_VIEWER_REQUEST or context == IContextMenuInvocation.CONTEXT_PROXY_HISTORY:
            req_res = invocation.getSelectedMessages()[0]
            comment = req_res.getComment()
            req = self.helper.analyzeRequest(req_res.getRequest())

            try:
                req_url = req.getUrl().toString()
            except:
                req_url = req.getHeaders()[0].split(" ")[1]

            menu_name = "Add comments about this url"
            menu_item = JMenuItem(menu_name, actionPerformed = CommentUrlPopupService.CommentUrlPopupService(self.config, self.packet_manager).onClickContextMenu)
            menu_item.putClientProperty("request_url", req_url)
            menu_item.putClientProperty("comment", comment)
            menu_item.putClientProperty("set_comment_func", req_res.setComment)

            return [menu_item]
