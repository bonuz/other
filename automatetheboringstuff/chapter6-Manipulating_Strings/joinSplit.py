# joinSplit.py
print(", ".join(["cats", "rats", "bats"]))
print(" ".join(["My", "name", "is", "Simon"]))
print("ABC".join(["My", "name", "is", "Simon"]))

print("My name is Simon".split("m"))
print("MyABCnameABCisABCSimon".split("ABC"))

#

spam = ''' Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experimient".

Please do not drink int.
Sincerely,
Bob'''
print(spam.split("\n"))
