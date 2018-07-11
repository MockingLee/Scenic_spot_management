# -*- coding: UTF-8 -*-
from fun.graph import *
from fun.stack import *
from fun.queue import *
from fun.dbFun import *
import datetime
g = Graph()
port = Stack(10)
quit = Stack(10)
wait = Queue()

# def fileReader(node_file_name, edge_file_name):
#     node_file = open(node_file_name, encoding='UTF-8')
#     edge_file = open(edge_file_name, encoding='UTF-8')
#     node_count = 0
#     while 1:
#         line = node_file.readline().strip('\n')
#         node_count += 1
#         if line is "":
#             break
#         else:
#             g.insertNode(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2], line.split(" ")[3],
#                          line.split(" ")[4])
# 
#     while 1:
#         line = edge_file.readline().strip('\n')
#         if line is "":
#             break
#         else:
#             g.insertEdge(line.split("——")[0], line.split("——")[1], line.split("——")[2])
#             inserEdge(line.split("——")[0], line.split("——")[1], line.split("——")[2])


def search(key):
    result = g.getNodeInfo(key)
    if result is {}:
        return False
    else:
        return result

def delete(name):
    if g.checkNodeExist(name):
        g.deleteNode(name)
        deleteNode(name)
        return True
    else:
        return False

def insert(name,description,popularity,rest_zone,toilet):
    if g.checkNodeExist(name):
        return False
    else:
        g.insertNode(name,description,popularity,rest_zone,toilet)
        inserNode(name,popularity,description,rest_zone,toilet)
        return True

def addEdge(name,dest,weight):
    if g.checkNodeExist(name):
        if g.checkNodeExist(dest):
            if int(weight) > 0:
                g.insertEdge(name,dest,weight)
                inserEdge(name,dest,weight)
                return True
    return False

def getShortestPath(start,end):
    print(start,end)
    if g.checkNodeExist(start) and g.checkNodeExist(end):
        return g.shortest_Path(start,end)
    else:
        return -1

def getRoute(start):
    if not g.checkNodeExist(start):
        return False
    else:
        return g.getRoute(start)


def carIn(car): ## use dict act as car data struct
    print(car)
    if not port.isFull():
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        car['timeIn'] = time
        port.push(car)
        carArrive(car['num'],time)
    else:
        carArrive(car['num'])
        wait.enqueue(car,None)

def carOut(carNumber):
    if not port.checkExist(carNumber):
        return False
    while True:
        current = port.pop()
        if current['num'] == carNumber:
            break
        quit.push(current)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current['timeOut'] = time
    carUpdateTimeOut(current['num'], time)

    while not quit.isEmpty():
        port.push(quit.pop())

    if not wait.is_empty():
        inItem = wait.dequeue()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        inItem['timeIn'] = time
        carUpdateTimeIn(inItem['num'],time)
        port.push(inItem)

    return current

def portState():
    return port.getArr()

def waitState():
    return wait.getArr()

def dbReader():
    node = getNodes()
    edge = getEdges()
    for i in node:
        g.insertNode(i[0],i[2],i[1],i[3],i[4])
    for i in edge:
        g.insertEdge(i[0],i[1],i[2])

dbReader()
g.showGraph()
# fileReader("./static/node_data.txt", "./static/edge_data.txt")






