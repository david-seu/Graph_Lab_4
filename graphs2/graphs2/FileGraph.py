from UndirectedGraph import Graph


def readFile(fileName):
    graph = Graph()
    with open(fileName, "r") as file:
        numberVertices, numberEdges = map(int, file.readline().split())
        for i in range(numberVertices):
            graph.addVertex(i)
        for _ in range(numberEdges):
            startVertex, endVertex, cost = map(int, file.readline().split())
            graph.addEdge(startVertex, endVertex, cost)
        file.close()
    return graph


def writeFile(fileName, graph: Graph):
    with open(fileName, "w") as file:
        file.write(str(graph.getNumberVertexes()) + ' ' + str(graph.getNumberEdges()) + '\n')
        edges = graph.parseEdges()
        for edge in edges:
            file.write(str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(edge[2])+'\n')
        file.close()
