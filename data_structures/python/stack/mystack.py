'''
The credit for the current implementation of the stack below goes to ---> https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html

'''
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
