from copy import deepcopy


dict1 = {"a":[1,2,3], "b":1, "c":4}
dict2 = deepcopy(dict1)

dict2["a"][0] = 4
print(dict1)