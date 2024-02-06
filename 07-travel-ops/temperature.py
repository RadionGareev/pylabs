try:
    temperatureC            = int(input("what'the outside tempereature in celsius degree?\n"))
except:
    exit("Incercati din nou, introduceti doar valoarea numerica")
if temperatureC         >= 20 and  temperatureC <= 30:    
    print("It's warm, more than 20 degreee C")
if temperatureC        >= 30  :
    print("It's hoty, more than 30 degreee C")
if temperatureC         <= 0:
   print("It's frozen time, less than 0 degreee C")
if temperatureC         <= 20 and temperatureC > 0 :
    print("It's cold, less that 20 degree celsius")
#else:
#    print("""ce ar trebui sa  fie in else?
#           ca la mine  nu se primeste  sa utilizez 
#           else, deoarece tot trebuie de mentionat in 
#          if. Altefel nu lucreaza correct""")
#   print("introduceti numai valori numerice")