from facepy import GraphAPI
from facepy import exceptions
from .FacebookRepositoryBase import FacebookRepositoryBase
from .Entities.FanCountDTO import FanCountDTO as FanCountDTO
from pymongo import MongoClient


class FacebookRepository(FacebookRepositoryBase):
    def __init__(self,accessToken,chosenVersion):
        self.Graph = GraphAPI(oauth_token=accessToken,version=chosenVersion)

    def GetFanCountByPageName(self,PageName):
        returns = []
        try:
            for val in self.Graph.get("/{0}/?fields=fan_count".format(PageName),page=True):
                returns.append(FanCountDTO(val['id'],val['fan_count']))
                return returns
        except exceptions.OAuthError:
            return []

    def InitMongoDB(self):
        DB_NAME = 'facebookexample'  
        DB_HOST = 'ds155631.mlab.com'
        DB_PORT =  55631
        DB_USER = 'test' 
        DB_PASS = 'test123'

        connection = MongoClient(DB_HOST, DB_PORT)
        db = connection[DB_NAME]
        db.authenticate(DB_USER, DB_PASS)
        self.Db = db
        self.Client=connection

    def SaveFanCountToDB(self,fanCountDTO):   
            self.InitMongoDB()
            self.Db.testcollection.insert_one(fanCountDTO.ToDict())
            self.Client.close()

    def GetAllRecordsFromDB(self):
            self.InitMongoDB()
            cursor = self.Db.testcollection.find()
            returns = []
            for document in cursor:
                returns.append(FanCountDTO(document['Id'],document['FanCount']))
            self.Client.close()
            return returns


