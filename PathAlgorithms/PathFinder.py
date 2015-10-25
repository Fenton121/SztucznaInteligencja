from ImageProcessing import ImageProcessing
from BestSearch import BestSearch

class PathFinder():
    def bestSearch(self):
        self.loadImage()
        
        bestSearch = BestSearch(self.imageProcessing.getOccupiedPoints(),
                                self.imageProcessing.getWeightsOfPoints(),
                                self.imageProcessing.getDimension())
        
        listOfPaths = bestSearch.search()
        self.dispaly(listOfPaths)
        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()
        


    def dispaly(self,
                listOfPaths):
        self.imageProcessing.convertAndDisplay(listOfPaths)