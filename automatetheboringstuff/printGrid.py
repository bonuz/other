grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid(gridToPrint):
    print(gridToPrint)
    print(len(gridToPrint))
    line = ""
    for x in range(len(gridToPrint[0])):
        for y in range(len(gridToPrint)):
            line = line + gridToPrint[y][x]
        print(line)
        line = ""
        

printGrid(grid)
print("\n".join(map("".join, zip(*grid))))


