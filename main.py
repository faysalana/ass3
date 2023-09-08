# # #1
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
#     def balance(self):
#         stack = []
#         opening_brackets = "([{"
#         closing_brackets = ")]}"
#         expression = ''.join(self.elements) # i did it 1st without this and i got a big error
#
#         for char in expression: #i used self.elements but didn't work
#             if char in opening_brackets:
#                 stack.append(char)
#             elif char in closing_brackets:
#                 if not stack:
#                     return False
#                 top = stack.pop()
#                 if opening_brackets.index(top) != closing_brackets.index(char):
#                     return False
#
#         return len(stack) == 0
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
#
# s3= Stack()
# s3.push("(1+2)-3*[41+6]")
# print(s3.balance())
#
# s4= Stack()
# s4.push("(1+2)-3*]41+6[")
# print(s4.balance())
#
# class Node:
#     def __init__(self, info, next=None):
#         self.info = info
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0  # number of nodes in my LL
#
#     def addToTail(self, info):  # O(1)
#         n = Node(info)
#         if self.size == 0:  # LL is empty
#             self.head = n
#             self.tail = n
#             self.size += 1
#         else:
#             self.tail.next = n
#             self.tail = n
#             self.size += 1
#
#     def deleteHead(self):  # O(1)
#
#         if self.size == 0:
#             return None
#         if self.size == 1:
#             temp = self.head.info
#             self.head = None
#             self.tail = None
#             self.size = 0
#             return temp
#
#         temp = self.head.info
#         self.head = self.head.next
#         self.size -= 1
#         return temp
#
#
# class Queue:
#     def __init__(self):
#         self.elements = LinkedList()
#
#     def enqueue(self, item):
#         self.elements.addToTail(item)
#
#     def dequeue(self):
#         return self.elements.deleteHead()
#
#     # def palindrome(self):   3mltle linkedlist object is not iterable
#     #      new=[]
#     #      for i in self.elements:
#     #          new.append(i)
#     #          self.elements.reverse()
#     #      if new == self.elements:
#     #          return True
#     #      else:
#     #          return False
#     def palindrome(self):
#         new = []
#         current = self.elements.head
#         while current:
#             new.append(current.info)
#             current = current.next # i googled this, i forgot about next that i insisted on before
#
#         return new == new[::-1] #hon jarabet eno est3ml reverse dal ytl3le error fa jrbt both reverse functions w ma shta8al e5er she tzakart no fe te3et lstrings
#
#     def balance(self):
#         stack = []
#         o_sign = "([{"
#         c_sign = ")]}"
#         expression = ''
#
#         current = self.elements.head
#         while current:
#             expression += current.info
#             current = current.next
#
#         for char in expression:
#             if char in o_sign:
#                 stack.append(char)
#             elif char in c_sign:
#                 if not stack:
#                     return False
#                 top = stack.pop()
#                 if o_sign.index(top) != c_sign.index(char):
#                     return False
#
#         return len(stack) == 0
#
#
# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(5)
#
# print(q.palindrome())
#
# q2 = Queue()
# q2.enqueue(1)
# q2.enqueue(2)
# q2.enqueue(1)
#
# print(q2.palindrome())
#
# print("meowwwwwwwwww")
# q3=Queue()
# q3.enqueue("(1+2)-3*[41+6]")
# print(q3.balance())
# q4=Queue()
# q4.enqueue("(1+2)-3*[41+6}")
# print(q4.balance())

#Queue

# class Car:
#     def __init__(self, make, color, plate_number):
#         self.make = make
#         self.color = color
#         self.plate_number = plate_number
#
# class Node:
#     def __init__(self, car):
#         self.car = car
#         self.next = None
#
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.size = 0
#
#     def enqueue(self, item):  #https://www.geeksforgeeks.org/queue-linked-list-implementation/
#         temp = Node(item)
#
#         if self.rear is None:
#             self.front = self.rear = temp
#             self.size += 1 #krmel lnext
#             return
#         self.rear.next = temp
#         self.rear = temp
#         self.size += 1
#
#     def dequeue(self):
#         if self.isEmpty():
#             return None
#         temp = self.front
#         self.front = temp.next
#         self.size -= 1 #lnshel lnext w nrj3 ltail
#         if self.front is None:
#             self.rear = None
#         return temp.car
#
#     def get_size(self):
#         return self.size
#
#     def isEmpty(self):
#         return self.size == "0"
#
#     def front(self):
#         if not self.isEmpty():
#             return self.front.car
#         else:
#             return None
#
# c1 = Queue()
#
# while True:
#     print("\nCar Wash Menu:")
#     print("1. Add a car to the queue")
#     print("2. Finish washing a car")
#     print("3. How many in line")
#     print("4. Who is next")
#     print("5. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         make = input("Enter car make: ")
#         color = input("Enter car color: ")
#         plate_number = input("Enter car plate number: ")
#         car = Car(make, color, plate_number)
#         c1.enqueue(car)
#         print("Car added to the queue.")
#
#     elif choice == "2":
#         if not c1.isEmpty():
#             car = c1.dequeue()
#             print("Make: ", car.make)
#             print("Color: ", car.color)
#             print("Plate Number: ", car.plate_number)
#         else:
#             print("No cars in washing.")
#
#     elif choice =="3":
#         print(c1.get_size())
#
#     elif choice == "4":  #ma bda tzbt
#         next_car = c1.front()
#         if next_car:
#             print("Next car: ", next_car.make)
#         else:
#             print("No cars in line.")
#
#     elif choice == "5":
#         break
#
#     else:
#         print("Invalid Input.")

#Stack
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

