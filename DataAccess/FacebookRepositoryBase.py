from abc import ABC, abstractmethod

class FacebookRepositoryBase(ABC):
    @abstractmethod
    def GetFanCountByPageName(self,PageName,AccessToken):
        pass
    def SaveFanCountToDB(self,fanCountDTO):
        pass
    def GetAllRecordsFromDB(self):
        pass