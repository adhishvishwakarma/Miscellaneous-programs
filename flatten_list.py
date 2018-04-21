
# Flatten list with recursion

def flatten_list(l, x=[]):
    for i in l:
        if not isinstance(i, list):
            x.append(i)
        else:
            flatten_list(i, x)
    return x


print(flatten_list([[1,[2,[3]], [4,5]], [6,[7], 8], 9]))
