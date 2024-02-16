days =  ["mo", "tu","wd","th","fr","sa","su"]
temps = [10.0, 9.0, 8.0, 0.0, -5.0, -10, 0.0]
from os import system
#      for i in range(7):
#          if temps[i] <= 0:
#              sign = "*"
#          else:
#              sign =" "
#          print(sign, days[i], temps[i])
system("cls")
i = 0
while i < len(days):
    
    if temps[i] <= 0:
        sign = "*"
    else:
        sign =" "
    print(sign, days[i], temps[i])
    i+=1