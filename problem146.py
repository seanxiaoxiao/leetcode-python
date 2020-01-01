class Node:

    def __init__(self):
        self.prev = None
        self.next = None
        self.val = None
        self.key = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        if self.cache.get(key):
            node = self.cache[key]
            self._remove(node)
            self._head(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            node = self.cache[key]
            node.val = value
            node.key = key
            self.cache[key] = node
            self._remove(node)
            self._head(node)
        else:
            node = Node()
            node.val = value
            node.key = key
            self._head(node)
            self.cache[key] = node
            if len(self.cache.keys()) > self.capacity:
                del self.cache[self.tail.key]
                self._remove(self.tail)

    def _head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _remove(self, node):
        prev = node.prev
        next = node.next
        if self.head == node:
            self.head = next
        if self.tail == node:
            self.tail = prev
        if prev:
            prev.next = next
        if next:
            next.prev = prev

cache = LRUCache(3)
cache.put(2, 2)
cache.put(1, 1)
print(cache.get(2))
print(cache.get(1))
print(cache.get(2))
cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
print(cache.get(4))