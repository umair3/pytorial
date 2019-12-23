class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head: Node, tail: Node):
        head.next = tail
        self.head = head
        self.tail = tail


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        self.recently_used = LinkedList(head=Node(0, 0), tail=Node(0, 0))

    def add(self, node: Node):
        self.recently_used.head.next