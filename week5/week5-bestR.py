#過去銷售
salesStr = "14,23,26,17,17,12,24,19,10,18,22,31,19,16,22,28,20,27,20,32"
sales = salesStr.split(',')
for i in range(len(sales)):
	sales[i] = int(sales[i]) #把銷售數據轉成整數

#原本有的資訊
stgCost = 2 #缺貨成本: 指的是當有缺貨時，要給客人的折扣
invCost = 1000*0.073/365 #1000為買一個存貨的成本 # 把1000快拿去銀行存會有7.3%的年利率,而這邊算的則是一天的存貨成本
Q = 23 #每一次跟廠商叫貨的進貨量
I = 20 #期初 存貨

bestR = 0
costofbestR = 1000000000000000000000000000
for R in range(Q):
	totalcost = 0
	for s in sales:
		I-=s
		if I<0:
			totalcost+= (-I)*stgCost #如果存貨小於零 會有缺成本
			I+=Q
		elif I<R:  #如果存貨小於R 要訂貨
			I+=Q
		if I >0:	
			totalcost+= I*invCost 
	print(R,totalcost)
	if totalcost<costofbestR:
		bestR = R
		costofbestR = totalcost

print('bestR : ',bestR,'min cost',costofbestR)					