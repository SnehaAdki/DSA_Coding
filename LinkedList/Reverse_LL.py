# https://leetcode.com/problems/reverse-linked-list/submissions/2001431892/
# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.


class Node : 
    head = None
    def __init__(self , data = 0):
        self.data = data
        self.next = None

    def insert_node(self, node):
        if self.head == None:
            self.head = node
            return self.head
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        return self.head

    def print_value(self):
        temp = self.head 
        while temp != None:
            print( f"{temp}:{temp.data}->{temp.next} " )
            temp = temp.next

    def reverse(self):
        if self.head.next == None:
            return self.head
        temp = self.head
        next_n = temp.next
        temp.next = None
        while next_n != None:
            p = next_n.next 
            next_n.next = temp
            temp = next_n
            next_n = p
        self.head = temp
        return temp

n1 = Node()
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)
n6 = Node(5)
n7 = Node(6)

head = n1.insert_node(n2)
head = n1.insert_node(n3)
head = n1.insert_node(n4)
head = n1.insert_node(n5)
head = n1.insert_node(n6)
head = n1.insert_node(n7)

n1.print_value()
n1.reverse()
n1.print_value()


