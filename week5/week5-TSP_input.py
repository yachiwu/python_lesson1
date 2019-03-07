#旅行者問題上課範例  使用者輸入版本
#設定距離二微陣列
numLoc = int(input())
dst = []
for i in range(numLoc):
	dst.append(input().split())
	for j in range(numLoc):
		dst[i][j] = int(dst[i][j])
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