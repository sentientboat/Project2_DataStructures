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
to remove the head (which would be the least recently used bucket) should be O(1).

PS:I will leave the above lines as I wrote them to reflect what my thought process was.
I ralised too late ( I had almost the whol esystem implemented) that the key-bucekt dictionary
should also kept tidy, and remove from it the references to the buckets that are removed
from the queue.
To keep this O(1) I will generate another dictionary, that is the inverse of the
key-bucket one. This way when I remove a bucket I can input that bucket in this dict,
and get the key that would return it from the first dict. That way I can delete
that key without parsing the whole dict.

I realize now that having 2 dictionaries and a queue may be too much space, which
may go against the idea of keeping a small cache.
