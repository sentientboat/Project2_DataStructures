Since this is a bit complex I will define the steps one by one:
1. using a dict, count occurrences of each letter for a given string
2. Define a queue class that guarantees that all it's items are always in order
  (this is done in the "add_node" method, keeping lower frequencies closer
  to the head. Note: this list will work for List_node and for Huffman Nodes)
3. Using this queue, build the tree.
4.  Parse the tree calculating the appropiate code for each letter
5. Build a codifier and decodifier function using this tree.
5.5 Codifying the string is done via a dictionary, that is populated with
    code -> char values as the tree is parsed in point 4. This dict will be stored
    as an attribute of the tree class.


6 Decodifying the string is done by feeding the binary code to the tree as
    traversal instructions until a char is found.

Notes: This code can be greatly improved, but I simply did not have as much time
as I would have liked. For example I use two kinds of nodes interchangably, which
looks awful and could have been solved usen a 'Node' class and used inheritance
for subsequent node classes.

In any case, this whole code should be O(n) (although this n would have a pretty big
multiplier if we did not ignore constant values when calculating O)
Space complexity would be a function of the length of the string and how many different
characters are present:
  For example, a string with only one kind of character and length 1 would be O(1),
  The same character repeated 1000 times would be size O(1000) since I have to
  store the longer string. So let's say space complexity in this dimension (len(str)) is O(n).
  On the other hand, a long string with many different characters would mean storing
  an extra node in the tree for each char. So the other dimension (str variance) is O(n) .
  Since we can assume the longer the string, the more different chars we have,
  the result would be a space complexity of O(n^2)
  Worst case scenario we get a long string that uses all possible characters.

I noticed we are measuring the size of our encoded string after casting it to an int.
I guess it would be interesting to test passing a bytes object (as seen in many
  applications online) but I simply do not have time to figure it our, I hope this is sufficient.
