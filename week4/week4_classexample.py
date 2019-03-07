#給一個數字 判斷是是否為 2 的次方 並且說明它是幾次方
num = int(input('給一個數字:　'))
n = 0
#我寫的
# while True:
# 	if num == 2**n:
# 		print(num,'是2的',n,'次方')
# 		break
# 	else:
# 		n+=1
# 	if 2**n > num:
# 		print('沒找到')
# 		break

# m = 1
# k = 0
# while num>m:
# 	m*=2
# 	k+=1
# if m == num:
# 	print(num,"是2的",k,"次方")
# else: 
# 	print("找不到")						

m = num
k = 0
while m >1:
	if m%2 !=0:
		break
	m//=2
	k+=1
if m==1:
	print(num,"是二的",k,"次方")		
else:
	print("找不到")	