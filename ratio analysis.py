#Ratios measure the
# performance of a company by comparing one year’s figures against another.
grossprofit1= int(input("input gross profit of first year"))
netprofit1= int(input("input net profit of first year"))
sales1 = int(input("input number of sales of first year"))

grossprofit2= int(input("input gross profit of second year"))
netprofit2= int(input("input net profit of second year"))
sales2 = int(input("input number of sales of second year"))


choice= input("would you like to use GPM or NPM? GPM/NPM")
if choice == "GPM":
    profitability1 = (grossprofit1/sales1) *100
    profitability2 = (grossprofit2/sales2) *100
elif choice =="NPM":
    profitability1= (netprofit1/sales1)*100
    profitability2= (netprofit2/sales2)*100
else:
    print("error")

print(profitability1,":",profitability2)



