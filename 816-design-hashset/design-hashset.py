#Approach - Double hashing
#2-D table with rows identified by 'buckets' and columns identified by 'items'
#initializing empty buckets and not items for all the buckets
# after deciding location of the key, always check if bucket has been initialized before with other values or not

#Notes
#We are performing double hashing meaning first hash1 function to determine bucket and 2nd hash2 function to determine item
#making search,add, delete O(1)
#other methods are chaining/linear chaining/binary chaining. It means LL or BST inside array. Will not make 2nd searching O(1)
#Probing used only when data is sparsed 



class MyHashSet:
    def __init__(self):
        self.buckets = 1000
        self.items = 1000
        self.storage = [[] for _ in range(self.buckets)]

    def hash1(self,key):
        return key % self.buckets

    def hash2(self,key):
        return key // self.items
        
    def add(self, key: int) -> None:
        bucket = self.hash1(key)
        item = self.hash2(key)
        if not self.storage[bucket]:
            self.storage[bucket] = [False]*(self.items + 1 if bucket == 0 else self.items)
        self.storage[bucket][item] = True

    def remove(self, key: int) -> None:
        bucket = self.hash1(key)
        item = self.hash2(key)
        if not self.storage[bucket]:
            return
        self.storage[bucket][item] = False
               
    def contains(self, key: int) -> bool:
        bucket = self.hash1(key)
        item = self.hash2(key)
        if not self.storage[bucket]:
            return False
        return self.storage[bucket][item]
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)