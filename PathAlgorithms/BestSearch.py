from Path import Path

class BestSearch():
    def search(self,
               occupiedPoints,
               weightsOfPoints):
        startPoint = (10, 10)
        stopPoint = (1000, 1000)
        listOfPath = [Path(startPoint)]
        
        while not(listOfPath[0].getCoordinate != stopPoint):
            print "fajnie"
            #print "listOfPath[0].getCoordinate() = " + str(listOfPath[0].getCoordinate()) + " " + str(type(listOfPath[0].getCoordinate()))
            #print "stopPoint = " +  str(stopPoint) + " " + str(type(stopPoint))
        