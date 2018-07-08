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
        for (k, v) in self.edgeinfo.items():
            if key in k or key in v['description']:
                result[k] = self.edgeinfo[k]
        return result

    def getMatrix(self):
        nodeArr = []
        result = []
        for i in self.edgeinfo:
            nodeArr.append(i)
        for i in range(0, len(nodeArr)):
            lineArr = []
            for j in range(0, len(nodeArr)):
                if i == j:
                    lineArr.append(0)
                else:
                    if nodeArr[j] in self.edge[nodeArr[i]]:
                        lineArr.append(self.edge[nodeArr[i]][nodeArr[j]])
                    else:
                        lineArr.append(sys.maxsize)
            result.append(lineArr)
        return result

    def deleteNode(self, name):
        self.edgeinfo.pop(name)
        self.edge.pop(name)
        for (k, v) in self.edge.items():
            if name in v:
                v.pop(name)

    def checkNodeExist(self, name):
        if name in self.edgeinfo:
            return True
        else:
            return False

    def shortest_Path(self, s, e):
        nodeArr = []
        for i in self.edgeinfo:
            nodeArr.append(i)
        dist = [0 for i in nodeArr]
        path = [0 for i in nodeArr]
        set = [0 for i in nodeArr]
        v = -1
        for i in range(0, len(nodeArr)):
            if nodeArr[i] == s:
                v = i
        matrix = self.getMatrix()
        for i in range(0, len(nodeArr)):
            dist[i] = matrix[v][i]
            set[i] = False
            if i != v and int(dist[i]) < sys.maxsize:
                path[i] = v
            else:
                path[i] = -1
        set[v] = True
        dist[v] = 0
        for i in range(0, len(nodeArr) - 1):
            min = sys.maxsize
            u = v
            for j in range(0, len(nodeArr)):
                if not set[j] and int(dist[j]) < int(min):
                    u = j
                    min = dist[j]
                set[u] = True
                for w in range(0, len(nodeArr)):
                    if not set[w] and int(matrix[u][w]) < sys.maxsize and int(dist[u]) + int(matrix[u][w]) < int(
                            dist[w]):
                        (dist[w]) = int(dist[u]) + int(matrix[u][w])
                        path[w] = u
        end_num = -1
        for i in range(0, len(nodeArr)):
            if nodeArr[i] == e:
                end_num = i

        # trace back

        shortest_path = []
        trace_num = end_num
        shortest_path.append(end_num)
        while True:
            if path[trace_num] == -1:
                break
            shortest_path.append(path[trace_num])
            trace_num = path[trace_num]

        result = {}
        if len(shortest_path) == 1:
            result[nodeArr[shortest_path[0]]] = {"dest": nodeArr[shortest_path[0]], "weight": 0}
        for i in range(0, len(shortest_path) - 1):
            result[nodeArr[shortest_path[len(shortest_path) - 1 - i]]] = {
                "dest": nodeArr[shortest_path[len(shortest_path) - i - 1 - 1]],
                "weight": matrix[shortest_path[len(shortest_path) - i - 1]][
                    shortest_path[len(shortest_path) - i - 1 - 1]]}
        return result

    def prim(self,root):
        res = []
        map = self.getMatrix()
        numRoot = 0
        for i in self.edgeinfo:
            if i == root:
                break
            numRoot += 1

        seleted_node = [numRoot]
        candidate_node = []
        for i in range(0, len(self.edgeinfo)):
            if i != numRoot:
                candidate_node.append(i)


        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, sys.maxsize
            for i in seleted_node:
                for j in candidate_node:
                    if int(map[i][j]) < minweight:
                        minweight = int(map[i][j])
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res

    def primToPath(self,start):
        pathArr = []
        primArr = self.prim(start)
        currentNode = primArr[0][0]
        set = []
        for i in primArr:
            set.append(False)
        for i in range(0,len(primArr)):
            currentNode = primArr[0][0]
            for j in range(0,len(primArr)):
                if not set[j]:
                    if primArr[j][0] == currentNode:
                        pathArr.append(primArr[j])
                        currentNode = primArr[j][1]
                        set[j] = True
        return pathArr

    def getRoute(self,start):
        path = self.primToPath(start)
        nodePathArr = []
        nodePathArr.append(path[0][0])
        for i in path:
            nodePathArr.append(i[1])
        result = []
        nodeArr = []
        for i in self.edgeinfo:
            nodeArr.append(i)
        for i in range(0,len(nodePathArr) -1):
            result.append(self.shortest_Path(nodeArr[nodePathArr[i]] , nodeArr[nodePathArr[i+1]]))
        result.append(self.shortest_Path(nodeArr[nodePathArr[i+1]] , nodeArr[nodePathArr[0]]))
        return result
