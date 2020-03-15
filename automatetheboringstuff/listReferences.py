# list references, list works like cursors

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
print(cheese)
print(spam)
