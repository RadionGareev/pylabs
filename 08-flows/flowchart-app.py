#define variables
service_price       = 100
#define crypto-rates
bitcoin_rate    = 800000

#check  amount waterflow and print
client_cash_amount  = int(input('enter cash  amount:'))
if client_cash_amount >= service_price:
    print('Cash payment success!')
else:
    print("Cash payment failure")
    client_card_amount  = int(input('enter card  amount:'))

    if client_card_amount >= service_price:
        print("card Payment success")
    else:
        print("card payment failure")
        client_crypto_amount= int(input('enter crypto  amount:'))
        # calculate crypto amount
        client_crypto_amount = client_crypto_amount * bitcoin_rate
        if client_crypto_amount >= service_price:
            print("crypto Payment success")
        else:
            print("Crypto payment failure")