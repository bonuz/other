tableData = [["Apples", "Oranges", "Cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["Dogs", "Cats", "Moose", "Goose"]]

def printTable(table):
    colWidths = [0] * len(table) # creates a list containing the same number of 0 values as the number of inner lists in table
    rowCount = [0] * len(table[i])
    lenght = 0
    for i in range(len(table)):
        for ii in table[i]:
            if len(ii) > lenght:
                lenght = len(ii)
        colWidths[i] = lenght
        lenght = 0
    print(colWidths)
    print(max(colWidths))
    for i in range(len(table)):
        for ii in table[i]:
            rowCount[
    
    
    

printTable(tableData)

