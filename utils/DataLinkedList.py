class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None

class DataLinkedList:

    def __init__(self, head_node = Node(None)):
        self._head = head_node

