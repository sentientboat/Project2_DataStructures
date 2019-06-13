Implemented a simple linked list. THe last node is kept at the head of the list,
and each node stores it's hash and the previous node's.
Everything is pretty straightforward. O(n) complexity where n is the number of
nodes to be appended, O(n) also for printing the list.

Space complexity is O(n) where n is the number of blocks, we just create and append
a block every time, no need to hold data outside of the blocks either, we just drop
whatever data we produce into them.
