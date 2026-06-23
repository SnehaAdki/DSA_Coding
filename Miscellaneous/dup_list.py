# Find duplicates in a list.

def find_dup(list_val):
    hadh_map = {}
    for i in list_val:
        if i in hadh_map.keys():
            hadh_map[i] = hadh_map.get(i)+1
        else:
            hadh_map[i] = 1

    for key,val in hadh_map.items():
        if val >1 :
            print(key)

find_dup([10,20,10,20,30,20])
