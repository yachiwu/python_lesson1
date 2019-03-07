import math

# 取得基地台與城鎮距離
def get_distance(base_station, country_location):
    distance = math.sqrt(pow(int(base_station['x'])-int(country_location['x']), 2) + pow(int(base_station['y'])-int(country_location['y']), 2))
    return int(distance)

def get_available_data(statation, data, station_range):
    person = 0
    include = []
    for idx, each in enumerate(data):
        if (each['is_covered'] != True):
            distance = get_distance(statation, each)
            if (distance <= int(station_range)):
                person += int(each['person'])
                include.append(idx)
    return {'person': person, 'data': include}


# 答案結果
result_station = []
result_covered_person = 0

# 輸入基本資料
num_of_country, base_station, station_range = input('請輸入城鎮數量、基地台數量、涵蓋範圍：').split()

# 輸入城鎮資料
# 資料內容：x-axis、y-axis、人數、是否被涵蓋
country_location = []
for num in range(int(num_of_country)):
    x, y, person = input('請輸入第' + str(num+1) + '個城鎮資料：').split()
    country_location.append({'x': x, 'y': y, 'person': person, 'is_covered': False})

# 挑選每個基地台位置
for station in range(int(base_station)):
    # 目前選擇的基地台
    curr_station = -1
    curr_cover_person = 0
    curr_cover_location = []

    for index, location in enumerate(country_location):
        # 若城鎮未被選取且未被涵蓋，則可為基地台候選
        if (index not in result_station) and (location['is_covered'] != True):
            # 取得候選基地台資訊
            cover_data = get_available_data(location, country_location, station_range)
            
            # 等於取數字小所以不用異動
            if(int(cover_data['person']) > curr_cover_person):
                curr_station = index
                curr_cover_person = cover_data['person']
                curr_cover_location = cover_data['data']
    
    # 計算完成後，將答案加入當中
    result_station.append(curr_station)
    result_covered_person += int(curr_cover_person)

    # 將完成涵蓋範圍更新
    for each in curr_cover_location:
        country_location[each]['is_covered'] = True

# 印出答案
result = ''
for each in result_station:
    result = result + str(int(each)+1) + ' '
result += str(result_covered_person)
print(result)