class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None: #checking to make sure list is not empty
            current = node.next_node #place holder for current next_node value
            node.next_node = prev #setting pointer of next_node to place holder "prev"
            self.reverse_list(current, node) #calling fn passing current value in as node, 
                # comparing = None, setting next_node to current ---- also passing in
                #current node and setting next_node pointer to prev --- then calling fn again

        else:
            self.head = prev #list only has 1 thing in it...

