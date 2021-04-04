# The main goal of this function is to implement a hash table with functions insert delete lookup
class Hashtable:
    # Intialisation class
    def __init__(self,length=10):
        self.map = [None]* length
    
    # The main goal of this function is to get a index in hash table 
    def _getHash(self,key):
        hash = 0
        for i in str(key):
            hash += ord(i)
        length = len(self.map)
        return hash % length
    
    # The main goal of this function is to add key values into hash table
    def add(self,key,value):
        if self.is_full():
            self.double()
        key_hash = self._getHash(key)
        key_value = [key,value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
            self.map[key_hash].append(key_value)
    
    # The main goal of this function is to get a value of specific key in hash table
    def get(self,key):
        hash = self._getHash(key)
        if self.map[hash] is not None:
            for val_pair in self.map[hash]:
                if val_pair[0] == key:
                    return val_pair[1]
        return None
    
    # The main goal of this function is to delete an value in hash table
    def delete(self,key):
        delete_hash = self._getHash(key)
        if self.map[delete_hash] is not None:
            for i in range(len(self.map[delete_hash])):
                if self.map[delete_hash][i][0] == key:
                    self.map[delete_hash].pop(i)
                    return True
        return False

    # The main goal of this function is to print the hash map
    def printHashmap(self):
        for item in self.map:
            if item is not None:
                print(item)
    
    # The main goal of this function is to check whether the hash map is full or not
    def is_full(self):
        items = 0
        for key in self.map:
            if key is not None:
                items += 1
        return items > len(self.map)/2

    # The main goal of this function is to double in hash table
    def double(self):
        map2 = Hashtable(length = len(self.map)*2)
        for i in range(len(self.map)):
            if self.map[i] is None:
                continue
            for kvp in self.map[i]:
                map2.add(kvp[0],kvp[1])
            self.map = map2.map

            
h = Hashtable()
h.add('a',1)
h.add('b',2)
h.add('c',3)
h.add('d',4)
h.add('e',5)
arr = h.map
print("hash table before deleting : ",arr)
h.delete('e')
arr1 = h.map
print("hash table after deleting : ",arr1)
print(h.get('c'))