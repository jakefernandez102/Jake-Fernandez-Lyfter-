class Node:
    data:any
    next:'Node'

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    head:Node
    def __init__(self):
        self.head = None

    def print_stack(self):
        if self.head is None:
            print("📂 Stack is empty.")
            return
        current_node = self.head
        while current_node:
            print(f'-> {current_node.data} 📀')
            current_node = current_node.next

    def pop(self):
        if self.head is None:
            print('Stack is empty')
            return
        popped_node = self.head
        self.head = self.head.next
        print(f"{popped_node.data} popped")
        return popped_node.data

    def push(self, new_node:Node):
        new_node.next = self.head
        self.head = new_node
        print(f"{new_node.data} inserted... 📀")


disc1 = Node('Disc 1')
disc2 = Node('Disc 2')
disc3 = Node('Disc 3')
disc4 = Node('Disc 4')

print('\n------inserting disc 1 and 2---------\n')

stack = Stack()

stack.push(disc1)
stack.push(disc2)
stack.print_stack()

print('\n------inserting disc 3---------\n')

stack.push(disc3)
stack.print_stack()

print('\n-----taking off last one----------\n')

stack.pop()
stack.print_stack()

print('\n------inserting disc 4---------\n')

stack.push(disc4)
stack.print_stack()
