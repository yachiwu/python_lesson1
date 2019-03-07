spend=int(input('客人給了 : '))
change=1000-spend
print('找零',change,'元')

five_hun =change//500
one_hun=((change%500)//100)
fifty=(((change)%100)//50)
ten=(((change%50)//10))
five=(((change%10)//5))
one=((change%5)//1)
dollars = []
dollars.append([500,five_hun])
dollars.append([100,one_hun])
dollars.append([50,fifty])
dollars.append([10,ten])
dollars.append([5,five])
dollars.append([1,one])
ans = ""
for d in dollars:
	if d[1] == 0:
		continue
	else:
	 ans+= str(d[0])+", "+str(d[1])+"; "		 
print(ans[:-2])	 #從最開始取到倒數第二個
print(five_hun, one_hun, fifty, ten, five, one)
print('500元找了',five_hun,'張')
print('100元找了',one_hun,'張')
print('50元找了',fifty,'張')
print('10元找了',ten,'張')
print('5元找了',five,'張')
print('1元找了',one,'張')
