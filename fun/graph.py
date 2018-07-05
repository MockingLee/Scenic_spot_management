import operator


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
        arr = self.getNodeArr()
        self.quick_sort(arr, 0, len(arr) - 1)

        return sorted(self.edgeinfo.items(), key=lambda x: x['popularity'], reverse=True)

    def bubble_sort(self):

        for i in self.edgeinfo:
            print(i)

    def selectSort(self):
        dict = self.edgeinfo
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
        if key in self.edgeinfo:
            return self.edgeinfo[key]
        else:
            return False

    def getMatrix(self):
        result = []
