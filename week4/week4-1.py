cost = int(input("單位成本"))
price = int(input("單位價格"))
max_demand = int(input("需求可能個數"))
quantity = int(input("訂貨量"))

Sale = 0.0
for demand in range (max_demand+1):
	prob = float(input("機率")) 
	if demand < quantity:
		Sale+= demand*price*prob
	else : 
		Sale+= quantity*price*prob
profit = Sale - cost*quantity
print(int(profit))		