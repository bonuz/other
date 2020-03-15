spam = {"color": "red", "age": 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

print(spam.keys())
print(list(spam.keys()))

for k, v in spam.items():
    print("key: " + k + " Value: " + str(v))

print("name" in spam.keys())
print("Zophie" in spam.values())
print("color" in spam.keys())
print("color" not in spam.keys())
print("color" in spam)

# the get() method

picnicItems = {"apples": 5, "cups": 2}
print("i am bringing " + str(picnicItems.get("cups", 0)) + " cups.")
print("i am bringing " + str(picnicItems.get("eggs", 0)) + " eggs.")

# the setdefault() method

spam = {"name": "Pooka", "age": 5}
#long way
if "color" not in spam:
    spam["color"] = "black"
print(spam)

spam = {"name": "Pooka", "age": 5}
#short way
spam.setdefault("color", "black")
print(spam)
#setdefault wont update or change the previour setdefault
spam.setdefault("color", "white")
print(spam)







