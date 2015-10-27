from ImageProcessing import ImageProcessing
from BestSearch import BestSearch

class PathFinder():
    def bestSearch(self):
        self.loadImage()
        
        bestSearch = BestSearch(self.imageProcessing.getOccupiedPoints(),
                                self.imageProcessing.getWeightsOfPoints(),
                                self.imageProcessing.getDimension())
        
        targetCoord, apexes = bestSearch.search()
        self.dispaly(targetCoord, apexes)
        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()
        


    def dispaly(self,
                targetCoord,
                apexes):
        self.imageProcessing.convertAndDisplay(targetCoord,
                                               apexes)