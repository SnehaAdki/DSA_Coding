# Reverse a string without using slicing.


def reverse(org):
    reversed = []
    for i in range(len(org)-1 ,-1,-1):
        reversed.append(org[i])

    print(''.join(reversed))

org = "Hello"
reverse(org)