# define currencies
currency_types = ["EUR","USD","MDL","RUB"]
#Introduce currency
currency_have = input(" Choose currency you would lie to exchange?(EUR/USD/MDL/RUB)\n")
currency_want = input(" what currency would you like  to buy?(EUR/USD/MDL/RUB)\n")
if currency_have in currency_types and currency_want in currency_types:
    pass
else:
    quit("Error: introduce the right currencies")
#Introduce money amount
try:
    amout      = int(input(" hou much money  wuould you like to exchange?: \n"))
except:
    exit("ERROR: introduce only digits. Try again please.")  
#currency rates
rates_to_MDL         = [19, 17, 1, 0.3]
#calculate currency any to MDL
if currency_want == "MDL":
    cur_rate_to_MDL = rates_to_MDL[currency_types.index(currency_have)]
    cur_to_mdl = cur_rate_to_MDL * amout
    cur_to_mdl = round(cur_to_mdl,2)
    print("you will get: ", cur_to_mdl, "MDL")
#calculate currency any to EUR via MDL
else:
    cur_rate_to_MDL = rates_to_MDL[currency_types.index(currency_have)]
    cur_to_mdl = cur_rate_to_MDL * amout
    cur_to_mdl = round(cur_to_mdl,2)
    print("you will get: ", cur_to_mdl, "MDL.\nWith this amount  you can buy: ")
    buy_other_currency = cur_to_mdl / rates_to_MDL[currency_types.index(currency_want)]
    buy_other_currency = round(buy_other_currency, 2)
    print(buy_other_currency," amount of ", currency_want)
