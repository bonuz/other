spam = [2, 5, 3.4, 1, -7]
spam.sort()
print(spam)
spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
# sort modifies the list, dont assing like this spam = spam.sort()
# cant sort a list that has both number and string values
# sort orders by ASCCIbetical order, so UPPER cases go first
spam = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
spam.sort()
print(spam)
spam = ["a", "A", "z", "Z"]
# but you can sort with key=str.lower
spam.sort(key=str.lower)
print(spam)
