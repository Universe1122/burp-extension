import dto.PacketInfo as PacketInfo

class PacketManager():
    
    def __init__(self):
        self.info = PacketInfo.PacketInfo()
    
    def getPacketInfo(self):
        return self.info.getInfo()
    
    def setPacketInfo(self, key, value):
        self.info.setInfo(key, value)