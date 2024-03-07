from map import *
from ui import *

# Initial position of 'R'
rr = 4
rc = 3
# Mine position
mr = 2
mc = 8

while True:
    clear()
    if mine<3:
        print("mine distance= ",mine)
    else:
        print("mine distance unknown")
    printMap(gameMap)

    key = controls()
    if key == 'x': 
        break

    # Check if the new position is within the boundaries of the map
    if 0 <= rr < len(gameMap) and 0 <= rc < len(gameMap[0]):
        gameMap[rr][rc] = 0  # Reset the previous position
        
        # Update the new position based on the key pressed
        if key == 'd' and rc + 1 < len(gameMap[0]) and gameMap[rr][rc + 1] != 1: 
            rc += 1
        elif key == 'a' and rc - 1 >= 0 and gameMap[rr][rc - 1] != 1: 
            rc -= 1
        elif key == 's' and rr + 1 < len(gameMap) and gameMap[rr + 1][rc] != 1: 
            rr += 1
        elif key == 'w' and rr - 1 >= 0 and gameMap[rr - 1][rc] != 1: 
            rr -= 1        
        gameMap[rr][rc] = 2  # Update the new position
        # Calculate the distance between 'R' and the mine
        distance = abs(rr - mr) + abs(rc - mc)
        
        # Check if 'R' is within the range of detecting the mine
        if distance <= 3:  # Adjust this range as needed
            mine = distance
            
        else:
            mine = 5  # Reset the mine detection
    else:
        pass
