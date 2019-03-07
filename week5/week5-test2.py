n = 8 #城鎮數量
p = 3 #基地台數量
d = 3 #基地台有效範圍
xy = [[3,-2],[-1,1],[-1,4],[3,2],[4,3],[-3,-4],[2,-3],[0,2]] #每個城鎮的座標
people = [10,15,10,20,20,25,15,10]
cover = [] #裝每一個城鎮涵蓋的範圍
coverpeople = []
maxpeople = -1 #來比較涵蓋人口用的	
route_final = [] #用來記錄建立順序的
count = 0 #紀錄目前有幾個基地台
for i in range(n):
	covertown = ""  #來記錄城鎮距離小於3的
	coverp = 0 #來記錄城鎮可容納人數
	for j in range(n):
		distance = ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**(0.5) #計算距離 (x1-x2)平方+(y1-y2)平方 然後開更號
		if distance <= d:
			covertown+= str(j+1)+' '
			coverp += people[j]	
	print(covertown)
	cover.append(covertown.split())
	coverpeople.append(coverp)

for i in range(len(coverpeople)):	
	if coverpeople[i] > maxpeople:
		maxpeople = coverpeople[i]	
		maxindex = i
print(maxpeople)	
print(maxindex)			
route_final.append(maxindex)
nowcovercity = cover[maxindex]
print('nowcovercity')
print(nowcovercity)
print('cover')
print(cover)

data=[]  #用來轉換nowcovercity
data2 = [] #用來轉換cover

for c in nowcovercity:
	print(c)
	data.append(c)
for city in cover:
	print(city)
	data2.append(city)
print(data)
print(data2)

for d in data:
	print(d)
	for c in data2:
		if d in c:
			c.remove(d)
		print(c)
print(data2)		


	

	

		




