import json

class Config():

    def __init__(self):
        self.save_file_name = "./config/packet_info.json"
    
    def savePacketInfo(self, data):
        with open(self.save_file_name, "w") as fp:
            json.dump(data, fp)
        
    def readPacketInfo(self):
        with open(self.save_file_name, "r") as fp:
            return json.loads(self.fp, encoding="cp949")