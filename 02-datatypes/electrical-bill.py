#inputs
c_name      =   input('Your name: ')
c_address   =   input('Your address: ')
c_e_index_0 =   int(input('before(kWh)'))
c_e_index_1 =   int(input('month 1(kWh)'))
c_e_index_2 =   int(input('month 2(kWh)'))
c_e_index_3 =   int(input('month 3(kWh)'))
c_e_index_4 =   int(input('month 4(kWh)'))
#operations
ec_price_1kwh   =   5
c_e_month_1kwh  =   c_e_index_1 - c_e_index_0   
c_e_month_2kwh  =   c_e_index_2 - c_e_index_1   
c_e_month_3kwh  =   c_e_index_3 - c_e_index_2   
c_e_month_4kwh  =   c_e_index_4 - c_e_index_3

c_e_bill_m1     =   c_e_month_1kwh * ec_price_1kwh
c_e_bill_m2     =   c_e_month_2kwh * ec_price_1kwh
c_e_bill_m3     =   c_e_month_3kwh * ec_price_1kwh
c_e_bill_m4     =   c_e_month_4kwh * ec_price_1kwh

c_e_total_kwh   =   c_e_month_1kwh + c_e_month_2kwh + c_e_month_3kwh + c_e_month_4kwh
c_e_total_bill  =   c_e_bill_m1 + c_e_bill_m2 + c_e_bill_m3 + c_e_bill_m4

k_1             = int(100* c_e_month_1kwh / c_e_total_kwh)
k_2             = int(100* c_e_month_2kwh / c_e_total_kwh)
k_3             = int(100* c_e_month_3kwh / c_e_total_kwh)
k_4             = int(100* c_e_month_4kwh / c_e_total_kwh)

#output
print("Consumption:")
print("M1: ", c_e_month_1kwh, "kWh, Total money =", c_e_bill_m1)
print("M2: ", c_e_month_2kwh, "kWh, Total money =", c_e_bill_m2)
print("M3: ", c_e_month_3kwh, "kWh, Total money =", c_e_bill_m3)
print("M4: ", c_e_month_4kwh, "kWh, Total money =", c_e_bill_m4)
print("--"*15)
print("Total:", "kWh =", c_e_total_kwh, "total Money =", c_e_total_bill)
print("Usage graph:")
print(k_1, "percents", k_2, "percents", k_3, "percents", k_4,"percents")
print("visualmode:")
print("#"*k_1)
print("#"*k_2)
print("#"*k_3)
print("#"*k_4)
