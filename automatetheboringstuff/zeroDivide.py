def spam(divideBy):
    return 42 / divideBy

def spam1(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return("Error: Invalid argument.")


print(spam1(2))
print(spam1(12))
print(spam1(0))
print(spam1(1))
