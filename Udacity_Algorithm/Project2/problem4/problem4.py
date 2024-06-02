class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    output = False
    if user in group.get_users():
        return True
    for gp in group.get_groups():
        output = is_user_in_group(user,gp)
    return output

# Testing

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

is_user_in_group("sub_child_user",parent)



# Test 2, there is nothing in the user_group
santa = Group("santa")
sub_child.add_group(santa)

is_user_in_group("christmas",parent)

# Test 3, dog group is no added to parent
dog = Group("dog")
dog.add_user("happy")

is_user_in_group("happy",parent)
