# get the first non repeat number 
# input_val = [4,7,2,4,3,7,2,8,3,9]
# output = 8


def get_first_non_repeat(input_val):
    hash_map = {}
    for val in input_val:
        # if val in hash_map.keys():
        hash_map[val] = hash_map.get(val,0)+1

    for i in input_val:
        if hash_map[i] == 1:
            return i

    

input_val = [4,7,2,4,3,7,8,3,9]
print(get_first_non_repeat(input_val ))
