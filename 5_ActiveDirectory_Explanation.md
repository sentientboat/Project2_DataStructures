The idea here is that to check if something is in a group or any of it's subgroups I would have to check every item in each group's 'users' list.
This would be O(n) where n is the sum of all users in all the groups below the one I am checking.

So I guess the fastest way to check if a user is in a group would be to simply use dictionaries for everything.

I worry this may go agains the spirit of the exercise, since I am basically copying JSON. But this is the only thing I could think of. Perhaps the exercise was meant to be solved by implementing my own hash function and creating my own brand of dictionary?  In any case, let me know.
