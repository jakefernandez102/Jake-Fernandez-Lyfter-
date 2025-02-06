class Node:
    data:any
    next:'Node'

    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    head:Node
    def __init__(self, head):
        self.head = head

    def print_queue(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def dequeue(self):
        self.head = self.head.next

    def enqueue(self, new_node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

disc1 = Node('Soy disc 1')
disc2 = Node('Soy disc 2')
disc3 = Node('Soy disc 3')
disc4 = Node('Soy disc 4')

queue = queue(disc1)

queue.enqueue(disc2)
queue.print_queue()

print('\n---------------\n')

queue.enqueue(disc3)
queue.print_queue()

print('\n---------------\n')

queue.dequeue()
queue.print_queue()

print('\n---------------\n')

queue.enqueue(disc4)
queue.print_queue()
