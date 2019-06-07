class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    findings = False
    for sub in group.get_groups():
        findings = is_user_in_group(user, sub)

    return findings


# TEST CASES
# Empty groups: No users in these groups, should return false:
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
child.add_group(sub_child)
parent.add_group(child)

# Should return false
print("Is \"sub_child_user\" in here? {}".format(
        is_user_in_group("sub_child_user", parent)))

# After the subgroups are populated "sub_child_user" should return true:
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

print("Is \"sub_child_user\" in here now? {}".format(
        is_user_in_group("sub_child_user", parent)))

# Adding users to child, and checking for one of them in every group:
# should return True, True and False respectively
child.add_user("Kafka")
child.add_user("Olaf")

print(is_user_in_group("Olaf", parent))
print(is_user_in_group("Olaf", child))
print(is_user_in_group("Olaf", sub_child))
