The idea here is that to check if something is in a group or any of it's subgroups I would have to check every item in each group's 'users' list.
This would be O(n) where n is the sum of all users in all the groups below the one I am checking.

So the first step would be to change the 'users' list to be a set instead. Since checking if something in in a set is O(1)

The rest is a matter of checking the subgroups of the called group for the desired user and stopping the search as soon as a match is found.
