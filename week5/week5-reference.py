################ 用文件輸入數值 ########################

import math # 呼叫sqrt
print("----------------------------------\n")

# 輸入
#cit_bas_cov = "8 3 3" # 先用範例數據做測試
cit_bas_cov = input() # 實跑
cit_bas_cov_ls = cit_bas_cov.split()
city = int(cit_bas_cov_ls[0])
base = int(cit_bas_cov_ls[1])
coverDist = int(cit_bas_cov_ls[2])
print()
print("city =",city)
print("base =",base)
print("coverDist =",coverDist)
print()

# 先用範例數據做測試
#x = [3,-1,-1,3,4,-3,2,0] # 測試用
#y = [-2,1,4,2,3,-4,-3,2] # 測試用
#people = [10,15,10,20,20,25,15,10] # 測試用
#people = [10,15,10,20,20,25,15,10] # 測試用
#city_list = [1,2,3,4,5,6,7,8] # 測試用
#unvisited = [1,2,3,4,5,6,7,8] # 測試用

x = [0]
y = [0]
people = [0]  
unvisited = [] 
for i in range(1,city+1):
    xyp = input()
    xyp_ls = xyp.split()
    
    for j in range(len(xyp_ls)):
        xyp_ls[j] = int(xyp_ls[j])
    
    print("第"+str(i)+"個城鎮x、y座標、人口數: ", end="")
    print(xyp_ls)
    x.append(xyp_ls[0])
    y.append(xyp_ls[1])
    people.append(xyp_ls[2]) 
    unvisited.append(i) 
del(x[0],y[0],people[0])

################## 單一城鎮人口數比較 ###################

# 這部分對解題沒用，單純是過渡期的一個思考過程
# 首先在所有城鎮中，找出 「如果蓋在這裡，將可以覆蓋最多人」 的城鎮，然後設一個基地臺在那裡。
#route = []
#current_city = 1
#people_cover = 0
#people_max = 0
#print("people",people) # 檢查用

#for j in range(base): # 繼續如此直到挑出 p 個城鎮去設置基地臺為止。
#    people_max_temp = 0
#    for i in range(len(people)): # 找出最多人的city
#        if (i+1) in route:
#                continue
#        else:
#            if people[i] > people_max_temp:
#                people_max_temp = people[i]
#                current_city = i+1 # 因為城鎮從1開始起算
#            elif people[i] == people_max and people[i] != people_max_temp:
#            # 如果在任一時刻遇到有兩個以上的城鎮可以被選，就選編號較小的那個。
#                current_city = i+1
#    people_max = people_max_temp
#    route.append(current_city) # route加進最多人的city
#    people_cover += people_max_temp # 累計覆蓋人數
#    unvisited.remove(current_city) # 更新unvisited名單
#print("route:",route) # 測試用
#print("people_cover",people_cover) # 測試用

################ 計算城鎮間的距離 ########################

# 計算城鎮間的距離
d = [[0 for i in range(city)] for j in range(city)]
# 原文網址：https://itw01.com/V5T7EWB.html

# --- 這部分算一點點關鍵，所以刪除

##################### 基地台演算法 #######################

#d = [['0.00', '5.00', '7.21', '4.00', '5.10', '6.32', '1.41', '5.00'], ['5.00', '0.00', '3.00', '4.12', '5.39', '5.39', '5.00', '1.41'], ['7.21', '3.00', '0.00', '4.47', '5.10', '8.25', '7.62', '2.24'], ['4.00', '4.12', '4.47', '0.00', '1.41', '8.49', '5.10', '3.00'], ['5.10', '5.39', '5.10', '1.41', '0.00', '9.90', '6.32', '4.12'], ['6.32', '5.39', '8.25', '8.49', '9.90', '0.00', '5.10', '6.71'], ['1.41', '5.00', '7.62', '5.10', '6.32', '5.10', '0.00', '5.39'], ['5.00', '1.41', '2.24', '3.00', '4.12', '6.71', '5.39', '0.00']]
#d = [[...# 先用範例數據做測試
#route = [6,4,5,2,7,1,3,8] # 測試用
#people = [10,15,10,20,20,25,15,10] # 測試用

# 單一城鎮畫半徑，把包含在內的城鎮，將其人口數加總
route_final = []
people_cover_final = 0
cover_town = [[] for i in range(city)]
# 原文網址：https://itw01.com/V5T7EWB.html

for m in range(base):
    people_d = [0]*city # 各城鎮半徑內的人數 ## 因為每次跑range(base)前都要先歸零，不然會亂加到前一廻圈的數值，所以放這邊
    # --- 這部分很關鍵，所以刪除
    # 如果在半徑範圍內，就把人口總數加總，並且將城鎮群組化
#people_d = [25, 35, 35, 50, 40, 25, 25, 55] # 測試用
#cover_town = [[1, 7], [2, 3, 8], [2, 3, 8], [4, 5, 8], [4, 5], [6], [1, 7], [2, 3, 4, 8]] # 測試用    
    
    # 哪個城鎮的半徑範圍內有最多人
    # --- 這部分很關鍵，所以刪除
    # 擁有最多人口數者，丟進route_final
    # --- 這部分很關鍵，所以刪除                

print()
print("route_final",route_final)
print("people_cover_final",people_cover_final)

########## 找到列表中最大值 - 所有位置 ##################

'''
https://codeday.me/bug/20170701/33281.html
>>> a = [32, 37, 28, 30, 37, 25, 27, 24, 35, 55, 23, 31, 55, 21, 40, 18, 50,
             35, 41, 49, 37, 19, 40, 41, 31]
>>> a.index(max(a))
>>> a
9

max元素为55(位置9和12上的两个元素)
>>> m = max(a)
>>> [i for i, j in enumerate(a) if j == m]
[9, 12]

'''

###################### 二維list的坑 ####################  

'''
原文網址：https://itw01.com/V5T7EWB.html

《錯誤使用》
>>> lists = [[]] * 3
>>> lists[[], [], []]
>>> lists[0].append(3)
>>> lists[[3], [3], [3]]

What has happened is that [[]] is a one-element list containing an empty list, 
so all three elements of [[]] * 3 are (pointers to) this single empty list. 
Modifying any of the elements of lists modifies this single list. 
You can create a list of different lists this way:

《法一》
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists[[3], [5], [7]]

《法二》 列表生成式法
>>> list = [[0 for i in range(m)] for j in range(n)]

《法三》 使用模組numpy
import numpy as np
test = np.zeros((m, n), dtype=np.int)

'''


###################### 題目 ############################        
'''
# 輸入
城鎮 n 個，挑選 p 個城鎮設基地臺，基地台可覆蓋半徑 d 公里；
城鎮的 x 座標，y 座標，人口數 Pi；​	 

# 檢查條件 (看有沒有輸入錯誤)
# 因為輸入老師的文件，所以略過寫檢查條件這件事
2 ≤ n ≤ 1000; # 所有城鎮數
2 ≤ p ≤ n; # 選出的城鎮數至少2個
−100 ≤ xi ≤ 100; # 坐標
−100 ≤ yi ≤ 100; # 坐標
1 ≤ Pi ≤ 100; # 單一城鎮人口數
不會有兩個城鎮落在同一個地點;

# 輸出
根據貪婪演算法的優先順序，印出選出的城鎮的編號，最後輸出被覆蓋的總人數。

##########################################################

舉例來說，如果輸入是
8 3 3
3 -2 10
-1 1 15
-1 4 10
3 2 20
4 3 20
-3 -4 25
2 -3 15
0 2 10

則輸出應該是
8 1 6 105
'''
##########################################################