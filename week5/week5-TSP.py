#旅行者問題上課範例
#設定距離二微陣列
numLoc = 5 #有五個點
dst = [[0,9,6,7,4],
	[9,0,5,9,6],
	[6,5,0,3,1],
	[7,9,3,0,4],
	[4,6,1,4,0]]

origin = 0  #起點是0 
tour = [origin] #用來記錄走的路徑
tourlen = 0
unvisited = []
for i in range(numLoc):
	unvisited.append(i)
unvisited.remove(origin)	

#演算法
cur = origin 
for i in range(numLoc-1):
	next = -1 #要去的下一個點
	mindst = 999
	for j in unvisited:
		if dst[cur][j]<mindst:
			next = j
			mindst = dst[cur][j]
	unvisited.remove(next)
	tour.append(next)
	tourlen+= mindst		
	cur = next
	print(tour,tourlen)	
tour.append(origin)
tourlen += dst[cur][origin]
print(tour,tourlen)		