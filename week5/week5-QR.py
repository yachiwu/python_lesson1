# (Q,R)policy
Q = int(input('order quantity Q :'))
R = int(input('Reorder point R :'))
I = int(input('initial inventory :'))

print('inventory',I)
while True:
	sales = int(input('sales a day'))
	if I-sales>0:
		I = I-sales
	else:
		I = 0	
	if I<R:
		print('order')
		I = I+Q
	print('inventory',I)		