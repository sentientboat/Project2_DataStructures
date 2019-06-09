import os

def delver(path, desired_termination):
    container = []
    _delve(path, desired_termination, container)
    return(container)

def _delve(path, desired_termination, container):
    if os.path.exists(path):
        for sub in os.listdir(path):
            new_dir = os.path.join(path, sub)
            if os.path.isfile(new_dir):
                if sub.endswith(".c"):
                    container.append((sub, new_dir))

            elif os.path.isdir(new_dir):
                _delve(new_dir, desired_termination, container)
            else:
                print("WTF")
    else:
        print("ERROR: path can not be found")
        return(None)

entry_point = r"V:\Academics\Data Structures\testdir"

c = delver(entry_point, ".c")
print("RESULTS:")
for i in c:
    print(i[0] + "  :  " + i[1])

entry_point = r"V:\Academics\Data Structures\nonexistent"

print("TESTING FOR NONEXISTENT PATH:")
c = delver(entry_point, ".c")
print("RESULTS: ")
for i in c:
    print(i[0] + "  :  " + i[1])



"""
test = os.path.join(entry_point, 'subdir5')

print(os.path.isfile(test))
print(os.path.isdir(test))

a = True
for a in os.listdir(test):
    print(a
    )"""
