
class Node:
    data:any
    next_node:'Node'
    prev_node:'Node'
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoubleEndedQueue:
    head:Node
    tail:Node
    def __init__(self):
        self.head = None
        self.tail = None

    def push_right(self,new_node:Node):
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        print(f'\n{new_node.data} added on the right\n')


    def push_left(self,new_node:Node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        print(f'\n{new_node.data} added on the left\n')

    def pop_right(self):
        if self.tail is None:
            print('\nQueue Empty, nothing to pop from right!\n')
            return
        else:
            popped_node = self.tail.data
            self.tail = self.tail.prev_node
            if self.tail is not None:
                self.tail.next_node = None
            else:
                self.head = None
            print(f'\n{popped_node} popped\n')

    def pop_left(self):
        if self.head is None:
            print('\nQueue is empty, nothing to pop from left!!!\n')
            return
        popped_node = self.head.data
        self.head.next_node = self.head
        if self.head is not None:
            self.head.prev_node = None
        else:
            self.tail = None
        print(f'{popped_node} popped')

    def print_double_ended_queue(self):
        if self.head is None:
            print('Queue Empty, nothing to show')
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

egg1 = Node('Egg 1 🥚')
egg2 = Node('Egg 2 🥚')
egg3 = Node('Egg 3 🥚')
egg4 = Node('Egg 4 🥚')

double_ended_queue = DoubleEndedQueue()

double_ended_queue.push_right(egg1)
double_ended_queue.print_double_ended_queue()

double_ended_queue.push_right(egg2)
double_ended_queue.print_double_ended_queue()

double_ended_queue.push_left(egg3)
double_ended_queue.print_double_ended_queue()

double_ended_queue.push_left(egg4)
double_ended_queue.print_double_ended_queue()

double_ended_queue.pop_right()
double_ended_queue.print_double_ended_queue()
