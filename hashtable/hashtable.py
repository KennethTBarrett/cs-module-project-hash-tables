from linked_list import LinkedList
import warnings

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.size = 0



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load_factor = self.size / self.capacity
        return load_factor

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed = 5381
        for c in key:
            hashed = (hashed * 33) + ord(c)
        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash_index = self.hash_index(key)

        # Check if LinkedList is empty. If it is...
        if self.storage[hash_index].head == None:
            # Set the head to be our entry, change size.
            self.storage[hash_index].head = HashTableEntry(key, value)
            self.size += 1
            return None
        else:  # If it's not...
            # Set our current value to be our head.
            current = self.storage[hash_index].head
            # So long as there's a next value, check for key match.
            while current.next:
                if current.key == key:  # If match found...
                    current.value = value  # Update value.
                current = current.next  # Next
            # Set our next value to be an entry node.
            current.next = HashTableEntry(key, value)
            self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        current = self.storage[hash_index].head

        # If our head is the key, simply set new head to be the next.
        if current.key == key:
            self.storage[hash_index].head = self.storage[hash_index].head.next
            self.size -= 1  # Modify size.
            return None
        # So long as there's a next value...
        while current.next:
            # Go to next, with a pointer to the current node `prev`
            prev = current
            current = current.next
            # Check for key match
            if current.key == key:
                # Set pointer.
                prev.next = current.next
                self.size -= 1  # Alter size.
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        current = self.storage[hash_index].head
        # Check if we have an entry
        if current == None:
            return None
        # Check for key match, return value if found.
        if current.key == key:
            return current.value
        # Otherwise, search for our key match, and return value.
        while current.next:  # Traversing, checking for key match.
            current = current.next
            if current.key == key:  # If we find it...
                return current.value  # Return the value.
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Change our capacity.
        self.capacity = new_capacity
        # Set new storage.
        new_storage = [LinkedList()] * new_capacity

        for i in self.storage:  # For all items  in our existing storage...
            current = i.head  # Set current to be our head.
            while current:  # So long as current still exists...
                # We need to calculate our hash index based upon our new specified capcacity.
                hash_index = self.hash_index(current.key)
                if new_storage[hash_index].head == None:  # If the head exists,
                    # Set our hash table entry to be the head.
                    new_storage[hash_index].head = HashTableEntry(current.key, current.value)
                else:  # If it does not exist...
                    # Create our entry node from the current key and value.
                    entry_node = HashTableEntry(current.key, current.value)
                    # Assign its next value to be the head.
                    entry_node.next = new_storage[hash_index].head
                    # Set the head of our new storage (at hash index) to be our entry node.
                    new_storage[hash_index].head = entry_node
                # Go to next value
                current = current.next
        self.storage = new_storage  # Set our storage to be new_storage.
    

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")