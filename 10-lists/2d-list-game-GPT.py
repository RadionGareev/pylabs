from os import system

robo_r = 0
robo_c = 0
option = ''
hp = 100
over = False

gmap = [
    ['x', ' ', ' ', '⚠', ' '],
    [' ', ' ', '⚠', ' ', ' '],
    [' ', '⚠', ' ', ' ', ' '],
    [' ', ' ', '⚠', ' ', '⚠'],
    ['⚠', ' ', ' ', ' ', ' ']
]

def print_map():
    print('-' * 13)
    for row in gmap:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' ')
        print('|')
    print('-' * 13)

while option != 'x':
    system('cls')
    print_map()
    print("\n\nHP:", hp, '%')

    if hp < 1:
        over = True

    if over:
        print('Game Over!\n')
        break

    print('\nControls:\n\na = left\nd = right\nw = up\ns = down\n\nx = exit\n')

    option = input('>>> ')

    if option == 'd' and robo_c < len(gmap[0]) - 1:
        robo_c += 1
    elif option == 's' and robo_r < len(gmap) - 1:
        robo_r += 1
    elif option == 'a' and robo_c > 0:
        robo_c -= 1
    elif option == 'w' and robo_r > 0:
        robo_r -= 1

    if gmap[robo_r][robo_c] == '⚠':
        gmap[robo_r][robo_c] = '☠'
        hp -= 20
    else:
        gmap[robo_r][robo_c] = 'x'
