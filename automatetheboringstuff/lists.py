spam = ["cat", "bat", "rat", "elephant"]
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(["cat", "bat", "rat", "elephant"][3])
print("Hello " + spam[0])
print("The " + spam[1] + " ate the " + spam[0] + ".")
# a list in a list
spam = [["cat","bat"], [10,20,30,40,50]]
print(spam[0])
print(spam[0][1])
# negative indexes
spam = ["cat", "bat", "rat", "elephant"]
print(spam[-1])
print(spam[-3])
print("The " + spam[-1] + " is afraid of the " + spam[-3] + ".")
# list slices
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])
# list lenght
print(len(spam))
# changing values in a list with indexes
spam[1] = "aardvark"
print(spam[1])
spam[2] = spam[1]
print(spam)
spam[-1] = 123456
print(spam)
# list concatenation and list replication
print([1, 2,3] + ["a", "b", "c"])
print(["x", "y", "z"] * 3)
spam = [1, 2, 3]
spam = spam + ["a", "b", "c"]
print(spam)
# removing values from lists with del statements
spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
print(spam)
del spam[2]
print(spam)







