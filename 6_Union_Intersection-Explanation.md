First, I will build a generator that parses the whole list, returning it's nodes' values.
After that the problem is basically using that generator to populate sets as
appropriate.
Solving the union function is trivial using sets, just set.add() each element
to a new set and return it (This will not accept duplicates, however)
Also using sets, intersection could be solved using python built in function.
I assume doing that would be against the spirit of the exercise so I will
generate a set from the first list (I would use a dictionary but this is kind
of the same concept) and check every item from the second list to see if it should
be included in the intersection.

After getting the feedback, I still think using sets is a good and pythonic way
to solve both functions. What I've done is merely update them so they return
another linked list with the appropiate nodes.

Every function here is O(n), since we iterate over each item once, and checking
'x in set' is O(1).

Space complexity is also O(n), even when using sets the amount of space required
is going to be directly proportional to the amount of nodes.
