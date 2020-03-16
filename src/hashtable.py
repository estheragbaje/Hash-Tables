# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        #Use self._hash_mod(key) to get the index of the insertion
        index = self._hash_mod(key)
        #Check to see if there's a value at this index. If there is no value:
        if self.storage[index] is None:
        #make a LinkedPair with the key, value and set it at that index
          self.storage[index] = LinkedPair(key, value)
        else:
        #get the current index
          current_node = self.storage[index]
          while current_node:
            #if key at current node is the same as key of the data, we need to chain
            if current_node.key == key:
              current_node = current_node.next
            #insert the new linked pair at the end of the linked list.
              current_node.next = LinkedPair(key, value)
        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #retrieve the index of the insertion
        # index = self._hash_mod(key)

        # if not self.storage[index]:
        #   print('key is not found')
        #   return
        



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
         #get the index of the insertion
        index = self._hash_mod(key)
        # check to see if the value at the index is not None
        if self.storage[index] is not None:
            # loop through the linked list to find the key
            current_node = self.storage[index]
            while current_node is not None:
                # if the current linked node key == key return the value
                if current_node.key == key:
                    return current_node.value
                # increment current_node
                current_node = current_node.next
            # return None is a key matching the input key is not found
            return None
        # otherwise return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        # create a new storage with the size of the capacity
        new_storage = [None] * self.capacity
        # iterate over the data in current storage
        for i in range(self.storage):
            # copy over the element
            new_storage[i] = self.storage[i]
        # set the storage to the new storage (add ref)
        self.storage = new_storage

      



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
