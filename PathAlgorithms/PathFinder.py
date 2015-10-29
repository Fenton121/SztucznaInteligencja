from ImageProcessing import ImageProcessing
from BestSearch import BestSearch
import timeit
class PathFinder():
    
    def checkSomething(self):
        listOfApexes = []
        
        for i in range(1000000):
            listOfApexes.append(Apex((0, 0), (0, 0)))
            
        startApex = timeit.default_timer()
        for i in range(1000000):
            dupa = listOfApexes[i].getWeight() <  0
            if dupa == True:
                return 35
            
        stopApex = timeit.default_timer()
        print "apexTime = " + str(stopApex - startApex)
        
    def checkSomething2(self):
        listOfApexes = []
        elementOfList = [10, 10, 10, 10, 10]
        for i in range(1000000):
            listOfApexes.append(elementOfList)
            
        startApex = timeit.default_timer()
        for i in range(1000000):
            dupa = listOfApexes[i][0] <  0
            if dupa == True:
                return 35
            
        stopApex = timeit.default_timer()
        print "apex2Time = " + str(stopApex - startApex)
        
    def bestSearch(self):
        self.loadImage()
        
        #dupa = self.checkSomething()
        #dupa2 = self.checkSomething2()
        
        start = timeit.default_timer()
        
        bestSearch = BestSearch(self.imageProcessing.getOccupiedPoints(),
                                self.imageProcessing.getWeightsOfPoints(),
                                self.imageProcessing.getDimension())
        
        targetCoord, apexes = bestSearch.search()
        stop = timeit.default_timer()
        self.dispaly(targetCoord, apexes)

        print "time = " + str(stop - start)

        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()
        


    def dispaly(self,
                targetCoord,
                apexes):
        self.imageProcessing.convertAndDisplay(targetCoord,
                                               apexes)