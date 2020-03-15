# picnicTable.py

def printPicnic(itemsDict, leftWidth, rightWidth):
    print("Picnig items".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))
picnicItems = {"Sandwitches": 4, "Apples":12, "Cups":4, "Cookies": 8000}
printPicnic(picnicItems, 12,5)
printPicnic(picnicItems, 20, 6)
