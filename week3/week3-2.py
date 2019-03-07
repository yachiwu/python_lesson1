spend=int(input('客人給了 : '))
change=1000-spend
print('找零',change,'元')

five_hun =change//500
one_hun=((change%500)//100)
fifty=(((change)%100)//50)
ten=(((change%50)//10))
five=(((change%10)//5))
one=((change%5)//1)
ans = ""
if five_hun > 0:
	ans+= "500, " + str(five_hun) + "; "
if one_hun > 0:	
	ans+= "100, " + str(one_hun) + "; "
if fifty > 0:	
	ans+= "50, " + str(fifty) + "; "
if ten > 0:	
	ans+= "10, " + str(ten) + "; "
if five > 0:	
	ans+= "5, " + str(five) + "; "
if one > 0:	
	ans+= "1, " + str(one) 		

print(ans)		
print(five_hun, one_hun, fifty, ten, five, one)
print('500元找了',five_hun,'張')
print('100元找了',one_hun,'張')
print('50元找了',fifty,'張')
print('10元找了',ten,'張')
print('5元找了',five,'張')
print('1元找了',one,'張')


# print(c*500+d*100+e*50+f*10+g*5+h)