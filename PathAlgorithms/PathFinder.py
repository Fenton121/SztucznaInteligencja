from ImageProcessing import ImageProcessing

class PathFinder():
    
    def bestSearch(self):
        self.loadImage()
        self.searchBestPath()
        self.dispaly()
        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()

    def searchBestPath(self):
        print 'searchBestPath'
        
    def dispaly(self):
        self.imageProcessing.convertAndDisplay()