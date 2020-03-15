def commaCode(list):
    line = ""
    for i in range(len(list)):
        if i == 0:
            line = str(list[i])
        elif i == len(list) -1:
            line = line + " and " + str(list[i])
        else:
            line = line + ", " + str(list[i])
    return line

spam = ["apple", "orange", "anana", "banana"]
spem = [123,1234,77,23.5,9123,00]

print(commaCode(spam))
print(commaCode(spem))
