# -*- coding: utf-8 -*-
class Stack:

    def __init__(self,size):
        self.items = []
        for i in range(0,size):
            self.items.append({})
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == len(self.items) -1

    def push(self, item):

        self.items[self.top +1] = item
        self.top +=1

    def pop(self):
        res = self.items[self.top]
        self.items[self.top] = {}
        self.top -=1
        return res

    def peek(self):
        if not self.isEmpty():
            return self.items[self.top]

    def size(self):
        return len(self.items)

    def getArr(self):
        return self.items

    def checkExist(self,num):
        for i in self.items:
            if i != {}:
                if num == i['num']:
                    return True

        return False

