To be honest, I am a bit unclear on how the blockchain works. SO here is what I intended to implement:
The chain starts with a dummy block. With a previous hash of "0"
The "previous hash" is used to point to the previous block, I implemented this using a dictionary
To print the whole chain  we just traverse the whole chain as if it was a linked list
but using hashes in a dict instead of pointers.

I can't think of any limit cases, other than creating two blocks with the same info at the same time, which would give the same hash. I prevent this by forcing the script to
sleep after adding a node
