#參考老師的  最大的差別在於機率算法   第17行
cost = int(input('請輸入單位進貨成本'))
price = int(input('請輸入單位零售價格'))
max_demand = int(input('請輸入可能的需求數量')) #在這裡N 固定等於8
prob = [] #可能機率的清單

for i in range(max_demand+1):
	prob.append(float(input('可能的機率')))
#print(prob)	
max_profit = 0.0
max_quantity = 0
profit = 0.0

for quantity in range(max_demand+1):
	sales = 0.0
	sum_prob = 0.0 #機率和
	for demand in range(max_demand+1):
		if demand < quantity:
			sales+= price*demand*prob[demand]
		else :
			sales+= price*quantity*prob[demand]

	profit = sales-(cost*quantity)
	print(profit)		
			
	if profit > max_profit:
		max_profit = profit 
		max_quantity = quantity
			
		
	
print(max_quantity,int(max_profit))
