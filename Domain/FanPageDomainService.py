from .FanPageDomainServiceBase  import FanPageDomainServiceBase
from DataAccess.FacebookRepository import FacebookRepository
from .Entities.FanCount import FanCount
from DataAccess.Entities.FanCountDTO import FanCountDTO

class FanPageDomainService(FanPageDomainServiceBase):
    def __init__(self,accessToken,chosenVersion):
        self.facebookRepository=FacebookRepository(accessToken,chosenVersion)
    def GetFanCountByPageName(self,name):
        data = self.facebookRepository.GetFanCountByPageName(name)
        if data!=[]:
            return FanCount(data[0].Id,data[0].FanCount,name)
        else:
            return FanCount(0,0,"")
    def SaveFanCount(self,fanCount):
        fanCountToSave = FanCountDTO(fanCount.PageId,fanCount.FanCount)
        try:
            self.facebookRepository.SaveFanCountToDB(fanCountToSave)
        except Exception as e:
             e.args = (e.args[0] + ' Failed to connect to DB',)
             raise
    def GetAllRecords(self):
        try:
            data=self.facebookRepository.GetAllRecordsFromDB()
            return data
        except Exception as e:
             e.args = (e.args[0] + ' Failed to connect to DB',)
             raise

        