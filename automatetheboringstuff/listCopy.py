import copy
spam = ["a", "b", "c", "d"]
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# copy.deepcopy() will copy the inner lists as well
