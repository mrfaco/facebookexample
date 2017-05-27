import json

class FanCountDTO():
    def __init__(self,pageId,fanCount):
        self.Id=pageId
        self.FanCount=fanCount
    def ToDict(self):
        return {'Id':self.Id,'FanCount':self.FanCount}
