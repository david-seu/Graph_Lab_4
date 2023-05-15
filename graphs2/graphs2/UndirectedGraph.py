from random import randint

class Graph:

    def __init__(self, vertices=0):
        self.V = [vertex for vertex in range(vertices)]
        self.graph = []


    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST
    # using Kruskal's algorithm
    def KruskalMST(self):

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in self.V:
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is less than to V-1
        while e < len(self.V) - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

    def getNumberVertexes(self):
        return len(self.V)

    def parseVertices(self):
        return self.V
    def parseEdges(self):
        return self.graph

    def getNumberEdges(self):
        return len(self.graph)

    def __checkIfVertex(self, vertex):
        if vertex not in self.V:
            return False
        return True

    def checkIfEdge(self, first, second):
        if not (self.__checkIfVertex(first) and self.__checkIfVertex(second)):
            raise ValueError("No vertex with such id")
        for edge in self.graph:
            if (edge[0] == first and edge[1] == second) or (edge[1] == first and edge[0] == second):
                return True
        else:
            return False

    def addEdge(self, startVertex, endVertex, cost):
        if not (self.__checkIfVertex(startVertex) and self.__checkIfVertex(endVertex)):
            raise ValueError("No vertex with such id")
        if self.checkIfEdge(startVertex, endVertex):
            raise ValueError("Edge already exists")
        self.graph.append([startVertex, endVertex, cost])

    def addVertex(self, vertex):
        if self.__checkIfVertex(vertex):
            raise ValueError("Vertex already exists")
        self.V.append(vertex)

    def removeVertex(self, vertex):
        if not self.__checkIfVertex(vertex):
            raise ValueError("Vertex doesnt exists")
        self.V.remove(vertex)
        for edge in self.graph:
            if edge[0] == vertex or edge[1] == vertex:
                self.graph.remove(edge)

    def removeEdge(self, startVertex, endVertex, cost):
        if not self.checkIfEdge(startVertex, endVertex):
            raise ValueError("No such edge")
        self.graph.remove([startVertex, endVertex, cost])

    def generateRandom(self, nrVertices: int, nrEdges: int):
        nrEdges = min(nrVertices * (nrVertices - 1) // 2, nrEdges)
        self.V = [vertex for vertex in range(nrVertices)]
        for _ in range(nrEdges):
            inId = randint(0, nrVertices - 1)
            outId = randint(0, nrVertices - 1)
            cost = randint(0, 25)
            while self.checkIfEdge(inId, outId) or inId == outId:
                inId = randint(0, nrVertices - 1)
                outId = randint(0, nrVertices - 1)
            self.addEdge(inId, outId, cost)

    def generateGraphObj(self, objList):
        graph = Graph()
        for node in objList:
            graph.addVertex(node)
        addedEdges = set()
        #or node in objList:
            #for edge in self.parseEdgesVertex(node):
                #if edge and (edge[1], edge[0]) not in addedEdges:
                 #   #graph.addEdge(edge[1], edge[0], )
                  #  addedEdges.add(edge)
        return graph