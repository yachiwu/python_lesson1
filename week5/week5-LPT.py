n = int(input('number of job : '))  #有n個工作
m = int(input('number og machine : ')) #m台機器
pstr = input('processing times : ')
p = pstr.spilt('')
for i in range(n):
	p[i] = int(p[i])
load = [0] *m  #m台機器的工作
assignment = [0] *n 

for j in range(n):
	leastloadmachine = 0 #工作最少的機器是哪台
	leastload = load[0]
	for i in range(1,m):
		if load[i] < leastload:
			leastloadmachine = i
			leastload = load[i]
	load[leastloadmachine]+=p[j]	
	assignment[j] = leastloadmachine+1
print('job assignment:' +str(assignment))	
print('machine load:' + str(load))	
