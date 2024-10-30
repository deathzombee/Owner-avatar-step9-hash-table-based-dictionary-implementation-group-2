from dictabs import DictAbstract
# Declare a private node class
class _LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    # Define print format so we can call print(Node)
    def __str__(self):
        return f"{self.key}: {self.value}"

# Implement a dictionary using a doubly linked list.
class DllDict(DictAbstract):
    def __init__(self):
        # Construct an empty Dictionary
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        # Return the number of items stored in the dictionary
        return self._size

    # Implementing the python magic method __contains__
    def __contains__(self, key):
        # Return true if key is in the dictionary, False otherwise
        key == self._normalize_key(key)
        return self._find(key) is not None

    #Implementing the python magic method __getitem__
    #This function will help in using this sytax dict[key]
    #technically multiple parts: get& set: next & prev
    #peter vang
    #this return head from the find method. Method similar to last step but not needing the root because we are using linked list
    def __getitem__(self, key):
        #Given a key, return the next coresponding value. Raises a KeyError
        #if next or key is not in the map.
        key = self._normalize_key(key)
        node = self._find(key)
        if node is None:
            raise KeyError("Item does not exist")
        return node.value 
    # Gabriel
    def __iter__(self):
        """Return an iterator of all keys in the DllDict."""
        current = self.head
        while current:
            yield current.key
            current = current.next

    #Internal function that looks for the node with
    #the given specified value
    def _find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None


    #Lisa
    def __setitem__(self, key, value):
        key = self._normalize_key(key)
        current = self.head

        while current:
        #check if key matches existing key on the head node. If yes, update value.
            if current.key == key:
               current.value = value
               return
            current = current.next
        #If head is empty, set the head & tail to the new_node.
        new_node = _LLNode(key, value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #If the head isn't a match to key and isn't empty
        #assign new node to be after the tail, 
        #new nodes prev to be the tail, 
        #then replace tail with new node. Increment length.
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1


    #Remove a node from the tree with the indicated key
    #Return the value after removing the node
    #Raise a KeyError if the key is not in the map."

    #Lisa
    def pop(self, key):
        key = self._normalize_key(key)
        
        #if key does not exist __getitem will return error, 
        # otherwise it returns value associated with key
        value = self.__getitem__(key)
        
        #if key exists, use remove method to get rid of 
        # that node and decrement length
        self._remove(key)
        self._size -= 1
        return value

    # Gabriel Calderon
    def _remove(self, key):
        """Internal method to find and remove a node by its key and return its value."""
        node = self._find(key)  # Find the node associated with the key.
        if node is None:
            raise KeyError(f"Key '{key}' not found")

        value = node.value

        # Update pointers to unlink the node from the list.
        if node.prev:
            node.prev.next = node.next
        else:
            # If no previous node, the node is the head.
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # If no next node, the node is the tail.
            self.tail = node.prev

        return value

    # Gabriel Calderon
    def _normalize_key(self, key):
        """Return a normalized version of the key."""
        return key.strip().lower()

   
    #Peter Vang
    #returns all data until it goes to next pointer of tail being none and exiting while loop
    def values(self):
        """Return an iterable of all values in the BSTDict."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    # Gabriel Calderon
    def items(self):
        """Return an iterator of all items in the DllDict."""
        current = self.head
        while current:
            yield (current.key, current.value)
            current = current.next

    # Gabriel Calderon
    # Something to do with DLL
    # If we needed them we could implement
    # left and right pop, meet in the middle by
    # traversing from both sides etc
    def reverse_iter(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev
