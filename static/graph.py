
class Graph:
    edge = {}
    def insertNode(self,name):
        self.edge[name] = {}
    def insertEdge(self,name,dest,weight):
        self.edge[name][dest] = weight

    def showGraph(self):
        print(self.edge)
    def find(self,name1,name2):
        return(self.edge[name1][name2])
g = Graph()
g.insertNode("a")
g.insertNode("b")
g.insertEdge("a","b",10)
g.insertEdge("a","b",11)
g.showGraph()












