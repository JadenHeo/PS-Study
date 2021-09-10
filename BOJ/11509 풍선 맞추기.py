class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def delete(self, node):
        pass

    def print_all(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

N = int(input())
H = list(map(int, input().split()))
