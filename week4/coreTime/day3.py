grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]

checkLand = [[]]

def checkIsland()-> list:
    for y in range(len(grid)):
        for x in range(len(grid[1])):
            if grid[y][x] == "1":
                return [y, x]
            pass