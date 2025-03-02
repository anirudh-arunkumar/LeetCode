class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.least_used = Node(0, 0)
        self.most_used = Node(0, 0)
        
        self.least_used.next = self.most_used
        self.most_used.prev = self.least_used

    def remove(self, node):
        prev = node.prev
        n = node.next
        prev.next, n.prev = n, prev
    
    def insert(self, node):
        prev, n = self.most_used.prev, self.most_used
        prev.next = n.prev = node
        node.next, node.prev = n, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:

            lru = self.least_used.next
            self.remove(lru)
            del self.cache[lru.key]
