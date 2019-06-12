This is a fairly straightforward problem. Just recursively crawl through all the
tree and check each file for the desired termination. I will store a list of tuples
containing the path and name of the file and return that as an output

Time complexity is O(n) where n is the number of items below the chosen folder
(items include both files and folders). This is because all we have to do is
identify each item, point the function at it, and check if its a file with the
desired termination or we need to keep exploring the structure, so we only
touch each item once.

Size complexity would be O(n) where n is the number of items in the folder,
like with time complexity. Overall we will have a recursively generated frame
per each call to the delve function, for a worse case scenario of n (where each
  folder contains only another folder and so on until the end, so we can not
  dispose of any function calls until the last one is resolved)
