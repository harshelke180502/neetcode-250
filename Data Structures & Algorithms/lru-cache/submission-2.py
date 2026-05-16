class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        

    #Remove from the leftmost part(least recently used)
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev


    #Insert in the right most node or the most recently used node
    def insert(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev=node
        node.next=nxt
        node.prev=prev

    
    
    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #Because the cache value points to the node in the linkedlist
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        # here we check if the key is still present inside the cache
        # if it is still present then we remove the node and assign it with the updated or new value
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
       
        
