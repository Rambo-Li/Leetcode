class LRUCache:
    
    def __init__(self, capacity: int):
        self.usage = deque()
        self.capacity = capacity
        self.count = {}
        self.store = {}
        self.fill = 0

    def get(self, key: int) -> int:
        if key in self.store:
            self.count[key] += 1
            self.usage.append(key)
            return self.store[key]
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        if (key not in self.store) and self.fill == self.capacity:
            while self.usage:
                temp = self.usage.popleft()
                self.count[temp] -= 1
                if self.count[temp] == 0:
                    self.store.pop(temp)
                    break
        elif key not in self.store:
            self.fill += 1
        
        self.store[key] = value
        self.usage.append(key)
        self.count[key] = self.count.get(key, 0) + 1

# deque coupled with dict, deque provides O(1) add and remove, ordering is achieved by append， while dict(count) controls the removal. 

class dnode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.left = dnode()
        self.right = dnode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key:int) -> int:
        
        if key in self.d:
            self.d[key].next.prev = self.d[key].prev
            self.d[key].prev.next = self.d[key].next
            self.d[key].prev = self.right.prev
            self.d[key].next = self.right
            self.right.prev.next = self.d[key]
            self.right.prev = self.d[key]
            return self.d[key].val
        else:
            return -1
    
    def put(self, key:int, value:int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.d[key].next.prev = self.d[key].prev
            self.d[key].prev.next = self.d[key].next
            self.d[key].prev = self.right.prev
            self.d[key].next = self.right
            self.right.prev.next = self.d[key]
            self.right.prev = self.d[key]
        else:
            if self.capacity == 0:
                temp = self.left.next
                self.d.pop(temp.key)
                self.left.next = self.left.next.next
                temp.next.prev = self.left
            else:
                self.capacity -= 1
            
            node = dnode(key, value, self.right.prev, self.right)
            self.d[key] = node
            self.right.prev.next = node
            self.right.prev = node

# double linked list with dict, O(1) to get the node, O(1) to change ordering.

""" The essence of this problem is that if you want to have some properties no single data structure can provide, try multiple data structures at the same time."""
