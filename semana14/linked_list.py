
class Node:
    data:str
    node:'Node'

    def __init__(self,data, nextNode = None):
        self.data = data
        self.next = nextNode

class LinkedList:
    head: Node
    def __init__(self,head):
        self.head = head
    
    def print_linked_list(self):
        current_node = self.head

        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next

node1 = Node('Hola Soy nodo 1')
node2 = Node('Hola Soy nodo 2')
node3 = Node('Hola Soy nodo 3')
node4 = Node('Hola Soy nodo 4')

node1.next = node2
node2.next = node3
node3.next = node4

linked_list = LinkedList(node1)
linked_list.print_linked_list()
