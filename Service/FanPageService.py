from Domain.FanPageDomainService import FanPageDomainService
from .Entities.FanCountOutput import FanCountOutput

class FanPageService:
    def __init__(self,accessToken):
        self.domain=FanPageDomainService(accessToken,2.6)
    def GetFanCountFromPageAndSaveToDB(self,PageData):
        data = self.domain.GetFanCountByPageName(PageData['fb_handle'])
        if data.PageId!=0:
            outputData = FanCountOutput(data.PageId,data.FanCount,"saved",PageData['name'])
            self.domain.SaveFanCount(outputData)
        else:
            outputData = FanCountOutput(data.PageId,data.FanCount,"not saved",PageData['name'])
        return outputData
    def GetAllRecords(self):
        return self.domain.GetAllRecords()

