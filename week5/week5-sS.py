# (Q,R)policy
s = int(input(' reorder point -s :'))
S = int(input('S :'))
I = int(input('initial inventory :'))

print('inventory',I)
while True:
	sales = int(input('sales a day'))
	if I-sales>0:
		I = I-sales
	else:
		I = 0	
	if I<s:
		print('order')
		print('現在存貨是',I,'叫了',S-I)
		I = I + (S-I)
	print('inventory',I)		