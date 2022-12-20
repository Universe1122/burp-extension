from urlparse import urlparse
import re

import dto.PacketInfo as PacketInfo

class PacketManager():
    
    def __init__(self, config):
        self.info = PacketInfo.PacketInfo()
        self.info.info = config.readPacketInfo()
        self.URL_REGEX = "\/[0-9]+\/*"
    
    def getPacketInfo(self, url):
        return self.info.getInfo(url)

    def getPacketInfoAll(self):
        return self.info.getInfoAll()
    
    def setPacketInfo(self, key, value):
        self.info.setInfo(key, value)
    
    def init(self, req_res, helper):
        for message in req_res:
            req = helper.analyzeRequest(message.getRequest())
            
            try:
                req_url = req.getUrl().toString()
            except:
                req_url = req.getHeaders()[0].split(" ")[1]
            
            try:
                comment = self.info.getInfo(req_url)["comment"]
                message.setComment(comment)
            except:
                pass
        
    def parseUrl(self, url):
        path = urlparse(url).path
        match_list = re.compile(self.URL_REGEX).findall(path)

        if len(match_list) != 0:
            for d in match_list:
                d = d.replace("/", "")
                path = path.replace(d, "{{%d}}")
        
        return path