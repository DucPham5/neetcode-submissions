class Node:
    def __init__(self, key: int,value: int, next:'Node' = None, prev:'None' = None):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next
        
    
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity =capacity
        self.cache = {}
        self.tail = None
        self.head = None
        

    def get(self, key: int) -> int:
        if key in self.cache:
            
            node = self.cache[key]
            if self.tail == node:#if node is tail
                return node.value
            if self.head == node:
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.head is None and self.tail is None:#if our cache is empty
            self.head = self.tail = Node(key,value)
            self.cache[key] = self.head
        elif key in self.cache:#update and move node to back 
            self.cache[key].value = value
            if self.tail != self.cache[key]:#if its tail just update value 
                if self.cache[key].prev:
                    self.cache[key].prev.next = self.cache[key].next #
                else:
                    self.head = self.head.next
                if self.cache[key].next:
                    self.cache[key].next.prev =self.cache[key].prev

                #move node to back and set tail to node
                self.cache[key].prev = self.tail
                self.tail.next = self.cache[key]
                self.tail = self.cache[key]
                self.cache[key].next = None
        else: #add and update tail and remove least recently used
            self.cache[key] = Node(key,value)
            self.cache[key].prev = self.tail
            self.tail.next = self.cache[key]
            self.tail = self.cache[key]
            #remove head
            if len(self.cache) > self.capacity:
                temp = self.head
                self.head = temp.next
                self.head.prev = None
                temp.next = None
                self.cache.pop(temp.key)
            

            
        
