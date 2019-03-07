n =int(input('number of job : '))   # n 個工作
m = int(input('number og machine : '))  #m 台機器
p = []
for i in range(n):
	p.append(int(input()))
# print(p)	
# print(sorted(p))
p.sort(reverse = True)   #排序過由大到小
print(p)
load = [0]*m #m台機器的時間
assignment = [0] *n #工作被分配到的機器

for i in range(n):
	leastmachine = 0 #指的是第一台 但index = 0
	leastloadtime = load[0]
	for j in range(1,m):
		if load[j] < leastloadtime:
			leastmachine = j
			leastloadtime = load[j]
	load[leastmachine]+=p[i]	
	assignment[i] = leastmachine+1
print('job assignment:' +str(assignment))	
print('machine load:' + str(load))	
