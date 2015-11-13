from Apex import Apex
from Common import *
import copy

class BestSearch():
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        numOfApexes = len(listOfActualApexes)
        for apexIdx in range(numOfApexes):
            if(weightOfApex < listOfActualApexes[apexIdx][2]):
                return apexIdx
        return numOfApexes