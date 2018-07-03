from fun.graph import *
g = Graph()
def fileReader(node_file_name,edge_file_name):
    node_file = open(node_file_name,encoding='UTF-8')
    edge_file = open(edge_file_name,encoding='UTF-8')
    node_count = 0
    while 1:
        line = node_file.readline().strip('\n')
        node_count +=1
        if line is "" :
            break
        else:
            g.insertNode(line.split(" ")[0],line.split(" ")[1])

    while 1:
        line = edge_file.readline().strip('\n')
        if line is "":
            break
        else:
            g.insertEdge(line.split("——")[0],line.split("——")[1],line.split("——")[2])


fileReader("node_data.txt","edge_data.txt")


