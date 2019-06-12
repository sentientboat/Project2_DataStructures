Implemented a simple linked list. THe last node is kept at the head of the list,
and each node stores it's hash and the previous node's.
Everything is pretty straightforward. O(n) complexity where n is the number of
nodes to be appended, O(n) also for printing the list.

I can't think of any limit cases, nodes can be appended ad infinitum and since
we are only ever printing the list it's hard to find any malfunctions.
