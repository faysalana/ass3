# class Stack:
#     def __init__(self):
#         self.elements = []
#
#     def push(self, item):
#         self.elements.append(item)
#
#     def palindrome(self):
#         new=[]
#         for i in self.elements:
#             new.append(i)
#             self.elements.reverse()
#         if new == self.elements:
#             return True
#         else:
#             return False
#
#
#
# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(5)
#
# print(s1.palindrome())
#
# s2 = Stack()
# s2.push(1)
# s2.push(2)
# s2.push(1)
#
# print(s2.palindrome())

class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # number of nodes in my LL

    def addToTail(self, info):  # O(1)
        n = Node(info)
        if self.size == 0:  # LL is empty
            self.head = n
            self.tail = n
            self.size += 1
        else:
            self.tail.next = n
            self.tail = n
            self.size += 1

    def deleteHead(self):  # O(1)

        if self.size == 0:
            return None
        if self.size == 1:
            temp = self.head.info
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        temp = self.head.info
        self.head = self.head.next
        self.size -= 1
        return temp


class Queue:
    def __init__(self):
        self.elements = LinkedList()

    def enqueue(self, item):
        self.elements.addToTail(item)

    def dequeue(self):
        return self.elements.deleteHead()

    # def palindrome(self):   3mltle linkedlist object is not iterable
    #      new=[]
    #      for i in self.elements:
    #          new.append(i)
    #          self.elements.reverse()
    #      if new == self.elements:
    #          return True
    #      else:
    #          return False
    def palindrome(self):
        new = []
        current = self.elements.head
        while current:
            new.append(current.info)
            current = current.next # i googled this, i forgot about next that i insisted on before

        return new == new[::-1] #hon jarabet eno est3ml reverse dal ytl3le error fa jrbt both reverse functions w ma shta8al e5er she tzakart no fe te3et lstrings 



q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(5)

print(q.palindrome())

q2 = Queue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(1)

print(q2.palindrome())


