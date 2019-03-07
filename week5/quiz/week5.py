townnum = 8 #城鎮數量
machinenum = 3 #基地台數量
distance = 3 #基地台有效範圍
town_can_cover = [] #裝每一個城鎮涵蓋的範圍 現在是一個字串清單
town_can_cover_people = [0]*8 #用來裝每個城鎮可以涵蓋的人數
final = [] #用來記錄哪個城鎮設立基地台
finalpeople = 0
# print(town_can_cover_people)
xyp = [[3,-2,10],[-1,1,15],[-1,4,10],[3,2,20],[4,3,20],[-3,-4,25],[2,-3,15],[0,2,10]] #每個城鎮的座標跟涵蓋人口
for i in range(len(xyp)):
	covertown = ""  #來記錄城鎮距離小於3的
	for j in range(len(xyp)):
		d = ((xyp[i][0]-xyp[j][0])**2+(xyp[i][1]-xyp[j][1])**2)**0.5
		if d <= distance:
			covertown+=str(j)+' '
	town_can_cover.append(covertown.split())
print("town_can_cover",town_can_cover) #[['0', '6'], ['1', '2', '7'], ['1', '2', '7'], ['3', '4', '7'], ['3', '4'], ['5'], ['0', '6'], ['1', '2', '3', '7']] #城鎮群組化
#把每一個城鎮的涵蓋範圍轉成數字 也就是把town_can_cover清單裡面的數字轉成int
i = 0
for town in town_can_cover: 
	j = 0 #用來當索引
	for c in town:
		town_can_cover[i][j] = int(c)
		j+=1
	i+=1
		
visited = []#紀錄已經被基地台覆蓋的鎮	當基地台數量大於零就會執行 也就是說每找到一次基地台就要把基地台數量減一
while(machinenum>0):
	townindex = 0 #紀錄town 的索引
	for town in town_can_cover: 
		people = 0
		for c in town:
			if c not in visited:
				people+=xyp[c][2]
		town_can_cover_people[townindex] = people
		townindex+=1
	print(town_can_cover_people)	
	maxpeople = 0 #紀錄可以涵蓋最多人的鎮
	maxtownindex = 0 #紀錄可以涵蓋最多人鎮的索引
	for peoplenum in town_can_cover_people:
		if peoplenum >maxpeople:
			maxpeople = peoplenum
			maxtownindex = town_can_cover_people.index(maxpeople) #找可以涵蓋最多人鎮的索引		
	final.append(maxtownindex)
	finalpeople+=town_can_cover_people[maxtownindex] #把設立基地台城鎮加進去fianl中
	for i in town_can_cover[maxtownindex]:
		visited.append(i)
	print(visited)
	print(final,finalpeople)
	machinenum-=1

	




		



