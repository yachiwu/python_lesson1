a=int(input('客人給了 : '))
b=1000-a
print('找零',b,'元')
c=b//500
d=((b%500)//100)
e=(((b)%100)//50)
f=(((b%50)//10))
g=(((b%10)//5))
h=((b%5)//1)

print(c, d, e, f, g, h)
print('500元找了',c,'張')
print('100元找了',d,'張')
print('50元找了',e,'張')
print('10元找了',f,'張')
print('5元找了',g,'張')
print('1元找了',h,'張')

print(c*500+d*100+e*50+f*10+g*5+h)