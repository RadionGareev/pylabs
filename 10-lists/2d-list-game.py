robo_r = 0 
robo_c = 0
option = ''
hp = 100
over = False
from os import system
gmap = [
    ['x', ' ',' ','⚠',' '],
    [' ', ' ','⚠',' ',' '],
    [' ', '⚠',' ',' ',' '],
    [' ', ' ','⚠',' ','⚠'],
    ['⚠', ' ',' ',' ',' ']
]
while option!='x':
    system('cls')
    ############ RPINT  the MAP :
    print('-'*13)
    for r in range(5):
        print('|', end=' ')
        for c in range(5):
            print(gmap[r][c], end=' ')
        print('|')
    print('-'*13)
    print("\n\nHP: ", hp, ' %')         
    ######## GAME OVER :    
    if hp<1:
        over = True
    if over == True:
        print('Game Over !\n')
        break         
    ############# CONTROLS :
    print('\nControls :\n\na = left\nd = right\nw = up\ns = down\n\nx = exit\n' )
    option = input('>>> ')
    if option =='d' and robo_c <len(gmap[robo_c])-1:
        gmap[robo_r][robo_c] = ' '
        robo_c +=1
        if gmap[robo_r][robo_c] == '⚠':
            gmap[robo_r][robo_c] = '☠'
            hp -=20
        else:
            gmap[robo_r][robo_c] = 'x'  
    if option =='s' and robo_r <len(gmap[robo_r])-1:
        gmap[robo_r][robo_c] = ' '
        robo_r +=1
        if gmap[robo_r][robo_c] == '⚠':
            gmap[robo_r][robo_c] = '☠'
            hp -=20
        else:
            gmap[robo_r][robo_c] = 'x' 
    if option =='a' and robo_c >0:
        gmap[robo_r][robo_c] = ' '
        robo_c -=1
        if gmap[robo_r][robo_c] == '⚠':
            gmap[robo_r][robo_c] = '☠'
            hp -=20
        else:
            gmap[robo_r][robo_c] = 'x'  
    if option =='w' and robo_r >0:
        gmap[robo_r][robo_c] = ' '
        robo_r -=1
        if gmap[robo_r][robo_c] == '⚠':
            gmap[robo_r][robo_c] = '☠'
            hp -=20
        else:
            gmap[robo_r][robo_c] = 'x' 


               

