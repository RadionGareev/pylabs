rr=4
rc=3


gameMap=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]
gameMap[rr][rc] = 2
def p(c):
    print(c+" ", end="")
def printMap(m):
    for ri in range(10):
        for ci in range(10):
            if m[ri][ci] ==0:
                p('.')
            if m[ri][ci] ==1:
                p('#')
            if m[ri][ci] ==2:
                p('R')
            if m[ri][ci] ==3: # a mine
                p('.')
        print()
