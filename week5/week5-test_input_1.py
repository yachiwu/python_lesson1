#第五周 報童問題進階版 input.txt 是用來進行檔案讀取的
cost = int(input())
price = int(input())
max_demand = int(input()) # N 
salvage = int(input())
prob = [] #可能機率的清單

for i in range(max_demand+1):
	prob.append(float(input()))
print(prob)	
max_profit = 0.0
max_quantity = 0
profit = 0.0

for quantity in range(max_demand+1):
	sales = 0.0
	for demand in range(max_demand+1):
		if demand < quantity:
			sales+= (price*demand+salvage*(quantity-demand))*prob[demand]
		else :
			sales+= price*quantity*prob[demand]

	profit = sales-(cost*quantity)
	print(profit)		
			
	if profit > max_profit:
		max_profit = profit 
		max_quantity = quantity
			
		
print(max_profit)	
print(max_quantity,int(max_profit))
