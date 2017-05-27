from abc import ABC, abstractmethod

class FanPageDomainServiceBase(ABC):
    @abstractmethod
    def GetFanCountByPageName(self,name):
        pass
    def SaveFanCount(self,fanCount):
        pass
