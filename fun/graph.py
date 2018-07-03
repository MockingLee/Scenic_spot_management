class Graph:
    edge = {}
    edgeinfo = {}
    def insertNode(self, name,description):
        self.edge[name] = {}
        self.edgeinfo[name] = description
    def insertEdge(self, name, dest, weight):
        self.edge[name][dest] = weight
        self.edge[dest][name] = weight

    def showGraph(self):
        print(self.edge)

    def getWeight(self, name1, name2):
        return (self.edge[name1][name2])

    def find(self,name):
        return self.edgeinfo[name]
