import sys
sys.path.append("/home/fenton/workspace/SztucznaIngeligencja/SztucznaInteligencja/View/")
sys.path.append("/home/fenton/workspace/SztucznaIngeligencja/SztucznaInteligencja/PathAlgorithms/")
sys.path.append("/home/fenton/workspace/SztucznaIngeligencja/SztucznaInteligencja/Images/")

from PathFinder import PathFinder

if __name__ == "__main__":
    pathFinder = PathFinder();
    pathFinder.searchBestPath()

    


