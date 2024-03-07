from os     import system
mine=5
def clear():
    system('cls')
def controls():
    print('use a,d,s,w, for movement')
    #if mine<4:
    #    print("Radar feel a mine in:", mine,' miles')
    key = input('>> ')
    return key