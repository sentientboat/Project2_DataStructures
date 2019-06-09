As far as I can see this problem has two parts:
1. Building a cache
2. Keeping track of the usage of each item

To not make this exercise too long I will use python's built-in dict to map each
key to a bucket.
Each bucket will hold the data that we want to keep in the cache, and two pointers
to 2 other buckets.
Using these buckets with pointers I will build a queue (it will work sort of like
a stack, nomenclature may be a bit confusing here). And every time a bucket
in this queue is used it will be moved to the head. This way when the cache reaches
maximum capacity the process of deleting keys from the dict and updating the queue
to remove the tail (which would be the least recently used bucket) should be O(1).

Of note is the fact that the buckets will store also the key that points to them,
that way deleting entries from the dictionary is as easy as calling
del dict[bucket.key]
