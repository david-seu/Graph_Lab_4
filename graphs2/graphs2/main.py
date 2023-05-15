"""# This is a sample Python script.
from GraphTraversal import manualTest1, manualTest2, randomTest

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Manual tests:")
    print(manualTest1())
    print(manualTest2())
    print("Random tests:")
    for _ in range(5):
        print(randomTest())

"""

from copy import deepcopy

from FileGraph import writeFile, readFile
from Vertex import Vertex
from UndirectedGraph import Graph


class Main():
    def __init__(self):
        self.__graph = Graph()
        self.__listGraphs = [deepcopy(self.__graph)]

    def menu(self):
        print("""
Commands:
    1. get the number of vertices
    2. get set of vertices
    3. add vertex
    4. add edge
    5. remove vertex
    6. remove edge
    7. check if edge exists
    8. copy graph
    9. go to last copy
    10. read from text file
    11. write to text file
    12. create random graph
    13. get edges
    14. get number edges
    15. Generate Minimum Spanning Tree
    0. exit
            """)
        commands = {
            1: self.nrVertices,
            2: self.getVertices,
            3: self.addVertex,
            4: self.addEdge,
            5: self.removeVertex,
            6: self.removeEgde,
            7: self.checkEdge,
            8: self.copyGraph,
            9: self.goLastCopy,
            10: self.readFrom,
            11: self.writeTo,
            12: self.generateGraph,
            13: self.getEdges,
            14: self.getNumberEdges,
            15: self.getMST
        }
        while True:
            inputCommand = int(input(">>"))
            try:
                if inputCommand == 0:
                    break
                elif inputCommand in range(1, 16):
                    commands[inputCommand]()
                else:
                    raise ValueError("Invalid Input")
            except Exception as e:
                print(e)

    def nrVertices(self):
        print(self.__graph.getNumberVertexes())

    def getVertices(self):
        print(self.__graph.parseVertices())

    def addVertex(self):
        id = int(input("id>>"))
        self.__graph.addVertex(Vertex(id))

    def addEdge(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        cost = int(input("cost>>"))
        self.__graph.addEdge(Vertex(inId), Vertex(outId),cost)

    def removeVertex(self):
        id = int(input("id>>"))
        self.__graph.removeVertex(Vertex(id))

    def removeEgde(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        cost = int(input("cost>>"))
        self.__graph.removeEdge(Vertex(inId), Vertex(outId),cost)

    def checkEdge(self):
        inId = int(input("inId>>"))
        outId = int(input("outId>>"))
        print(self.__graph.checkIfEdge(Vertex(inId), Vertex(outId)))

    def copyGraph(self):
        self.__listGraphs.append(deepcopy(self.__graph))

    def goLastCopy(self):
        self.__graph = self.__listGraphs.pop(-1)

    def readFrom(self):
        fileName = input("fileName>>")
        self.__graph = readFile(fileName)

    def writeTo(self):
        fileName = input("fileName>>")
        writeFile(fileName, self.__graph)

    def generateGraph(self):
        nrVertices = int(input("nrVertices>>"))
        nrEdges = int(input("nrEdges>>"))
        self.__graph.generateRandom(nrVertices, nrEdges)

    def getEdges(self):
        print(self.__graph.parseEdges())

    def getNumberEdges(self):
        print(self.__graph.getNumberEdges())

    def getMST(self):
        self.__graph.KruskalMST()


if __name__ == "__main__":
    main = Main()
    main.menu()


