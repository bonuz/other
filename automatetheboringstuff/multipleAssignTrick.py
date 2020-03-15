cat = ["fat", "orange", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]
# or with the trick
size, color, disposition = cat
# must respect viables and lenght of list

# can use this to swap variables
a, b = "alice", "bob"
a, b = b, a
print(a)
print(b)
