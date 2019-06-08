class Bucket:
    def __init__(self, key, data):
        self.previous = None
        self.next = None
        self.key = key
        self.data = data


class LRU_Queue:

    def __init__(self, cacheDict, max = 10):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max
        self.dict = {}
        self._cacheDict = cacheDict


    def update(self, bucket):
        previous_bucket = bucket.previous
        next_bucket = bucket.next
        if previous_bucket is None:  # We are already dealing with the head.
            return

        if next_bucket is None:
            # Link previous and next.
            previous_bucket.next = next_bucket
            # Move updated bucket to the head
            bucket.previous = None
            bucket.next = self.head
            self.head = bucket

        else:
            # Link previous and next.
            previous_bucket.next = next_bucket
            next_bucket.previous = previous_bucket
            # Move updated bucket to the head
            bucket.previous = None
            bucket.next = self.head
            self.head = bucket

    def add_bucket(self, key, new_bucket):
        if self.size == self.max_size:
            self._remove_LRU()

        # self.dict[new_bucket] = key
        if self.head is None:
            self.head = new_bucket
            self.tail = new_bucket
            self.size += 1

        else:
            new_bucket.next = self.head
            self.head.previous = new_bucket
            self.head = new_bucket
            self.size += 1

    def _remove_LRU(self):
        if self.size == 0:
            return  # Nothing to remove, so do nothing.
        elif self.size == 1:
            self._remove_cache_dict(self.tail.key)
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self._remove_cache_dict(self.tail.key)
            self.tail = self.tail.previous
            self.tail.next = None

    def _remove_cache_dict(self, key):
        del self._cacheDict[key]  # Removes entry from cache's dict.

    def print_in_order(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next


class LRU_Cache(object):

    def __init__(self, capacity=10):
        self.dict = {}
        self.queue = LRU_Queue(self.dict, capacity)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        retrieved = self.dict.get(key)
        if retrieved:
            self.queue.update(retrieved)
            return(retrieved.data)
        else:
            return -1

    def set(self, key, value):
        # If the item is already in the stack, update it and modify the queue.
        if key in self.dict:  # X in Dict is O(1)
            # rewrite bucket's value and update it's position
            bucket = self.dict[key]
            bucket.data = value
            self.queue.update(bucket)
        else:
            new_bucket = Bucket(key, value)
            self.dict[key] = new_bucket
            self.queue.add_bucket(key, new_bucket)

    def print_queue(self):
        print("This cache's use queue is:")
        self.queue.print_in_order()
        print("\n")

# TEST 1: General use.


our_cache = LRU_Cache(5)

our_cache.set(1, 'a')
our_cache.set(2, 'b')
our_cache.set(3, 'c')
our_cache.set(4, 'd')
print("THe queue should be d,c,b,a")
our_cache.print_queue()
print("For input 3, our cache returns: {}  Should be .\'c\'".format(our_cache.get(3)))
print("The queue should now be c,d,b,a")
our_cache.print_queue()
our_cache.set(5, 5)
our_cache.set(6, 6)
print("Let's see if the cache updated without increasing size:")
our_cache.print_queue()
print("For input 7, our cache returns: {}  Should be -1".format(our_cache.get(7)))
#our_cache.print_queue()

"""
print(our_cache.get(1))
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(1, 5)
our_cache.set(6, 6)
print(our_cache.get(1))
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.print_queue()
"""
