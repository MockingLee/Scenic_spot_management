import sys

class Graph:
    edge = {}
    edgeinfo = {}

    def insertNode(self, name, description, popularity, rest_zone, toilet):
        self.edge[name] = {}
        self.edgeinfo[name] = {'description': description, 'popularity': popularity, 'rest_zone': rest_zone,
                               'toilet': toilet}

    def insertEdge(self, name, dest, weight):
        self.edge[name][dest] = weight
        self.edge[dest][name] = weight

    def showGraph(self):
        print(self.edge)
        print(self.edgeinfo)

    def getWeight(self, name1, name2):
        return (self.edge[name1][name2])

    def find(self, name):
        return self.edgeinfo[name]

    def getSortResult(self):
        arr = self.getNodeArr().copy()
        self.quick_sort(arr, 0, len(arr) - 1)

        return sorted(self.edgeinfo.items(), key=lambda x: x['popularity'], reverse=True)



    def selectSort(self):
        dict = self.edgeinfo.copy()
        result = {}
        size = len(dict)
        for i in range(size):
            last_value = 0
            last_key = None
            for (key, value) in dict.items():
                if int(value['popularity']) > int(last_value):
                    last_value = value['popularity']
                    last_key = key
            dict.pop(last_key)
            result[last_key] = {'popularity': last_value}
        return result

    def quick_sort(self, array, l, r):
        if l < r:
            q = self.partition(array, l, r)
            self.quick_sort(array, l, q - 1)
            self.quick_sort(array, q + 1, r)

    def partition(self, array, l, r):
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    def getNodeArr(self):
        arr = []
        for i in self.edgeinfo:
            arr.append(int(self.edgeinfo[i]['popularity']))
        return arr

    def getNodeInfo(self, key):
        result = {}
        for (k,v) in self.edgeinfo.items():
            if key in k or key in v['description']:
                result[k] = self.edgeinfo[k]
        return result



    def getMatrix(self):
        nodeArr = []
        result = []
        for i in self.edgeinfo:
            nodeArr.append(i)
        for i in range(0,len(nodeArr)):
            lineArr = []
            for j in range(0,len(nodeArr)):
                if i == j:
                    lineArr.append(0)
                else:
                    if nodeArr[j] in self.edge[nodeArr[i]]:
                        lineArr.append(self.edge[nodeArr[i]][nodeArr[j]])
                    else:
                        lineArr.append(sys.maxsize)
            result.append(lineArr)
        return result


    def deleteNode(self,name):
        self.edgeinfo.pop(name)
        self.edge.pop(name)
        for (k,v) in self.edge.items():
            if name in v:
                v.pop(name)

    def checkNodeExist(self,name):
        if name in self.edgeinfo:
            return True
        else:
            return False