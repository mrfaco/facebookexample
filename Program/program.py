import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Service.FanPageService import FanPageService
from PagesToGet import PagesToGet

accessToken="EAACEdEose0cBAL1WE4ZCcYZBtoQcWAZBiSLsBXxHNDT6Edaq8T1ZBzEgoHZBMxszrZAmHbD2ljatRiPJwZA6LLkWqP5ZAxUmDEdVMiw3P7zeHNY5WNDJlVZBHyKwNyL12M3ePZAZB9TPUTR8pFrGAl65Os4i8JupkFBzQbB5kIlq6oZB3w8qmDnlUBn3ajOqYZCZBTkjMZD"
service=FanPageService(accessToken)

if 1:
    for page in PagesToGet().GiveMeSomePages():
        output = service.GetFanCountFromPageAndSaveToDB(page)
        print("ID:{0}, Fan Count:{1}, Result:{2}".format(output.PageId,output.FanCount,output.Status))

if 0:
    outputList = service.GetAllRecords()
    for out in outputList:
        print(out.Id,out.FanCount)

