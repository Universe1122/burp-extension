class PacketInfo():
    def __init__(self):
        self.info = dict()
        pass
    
    def setUrl(self, url):
        self.url = url
    
    def getUrl(self):
        return self.url
    
    def getInfo(self):
        return self.info
    
    def setInfo(self, key, value):
        self._setInfo(self.info, key, value)

    def _setInfo(self, data, key, value):
        try:
            tmp = data[key]
        except:
            data[key] = {}
        
        if type(value) == dict:
            for k in value.keys():
                self._setInfo(data[key], k, value[k])
        
        elif type(value) == list:
            if type(data[key]) != list:
                data[key] = list()
            
            data[key] += value
        
        else:
            data[key] = value