from ImageProcessing import ImageProcessing
from BestSearch import BestSearch
import timeit
from time import time

class PathFinder():
    def bestSearch(self):
        self.loadImage()
        
        t0 = time()

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