# a = ["fsdjfkls", "啊啊啊", "不不不"]
# b = ["1", "2", "3"]
# c = dict(zip(a, b))
# d = list(zip(a, b))
# print(d)
# print(c)

# 字典推导式
# import random
# randomdict = {i:random.randint(10,100) for i in range(1,10)}
# print(randomdict)


#
#
# alien_0 = {'color': 'green', 'points': 5}
#
# # 字典查询
# print(alien_0['color'])
# print(alien_0['points'])
#
# # 字典增加
# # 直接字典加key 把value赋值给key
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# # 字典修改  对原来的key重现赋值  跟添加一样  类似覆盖旧的
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")


alien_0 = {'x_position': 0,
           'y_position': 25,
           'speed': '321'
           }
# 旧位置
print(f"Original x-position: {alien_0['x_position']}")

# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    alien_0["speed"] = 'fast'  # 修改为fast
    x_increment = 3

# 新位置为旧位置加上移动距离。
# alien_0['x_position'] += x_increment
# # 输出新位置
# print(f"New position: {alien_0['x_position']}")
# print(f"现在的速度{alien_0['speed']}")
# print(alien_0)
#
#
# # 字典删除
#
# alien_0 = {'color': 'green',
#            'points': 5}
# print(alien_0)
#
#
# alien_0["haha"] = 11
# print(alien_0)

# 删除键值对
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

#
# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['points'])
# # 字典查询  查询的值不存在时不会报错  可以设定默认值
# # print(alien_0.get("color","dasdasdas"))
# print(alien_0.get("colo"))


# 遍历字典
#
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
#
# print(user_0.items())  #以元组形式输出字典内的内容
#
# for key,value in user_0.items():
#     print(key,value)
#     # print(value)
# print(type(user_0.items()))

#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#
# }
#
# for name in set(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


# favorite_languages = {
#         'jen': 'python',
#         'sarah': 'c',
#         'edward': 'ruby',
#         'phil': 'python',
#
#      }
#
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#       print(language.title())


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#       print(alien)

# 创建一个用于存储外星人的空列表。
aliens = []

# # 创建30个绿色的外星人。
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# # 显示前5个外星人。
# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# # 显示创建了多少个外星人。
# print(f"Total number of aliens: {len(aliens)}")




#
# # 创建30个绿色的外星人。
#
# aliens = []
# for alien in range(1,30):
#     new_alien = {"name":"1111","yanse":"green"}
#     aliens.append(new_alien)
# print(aliens)
# # 显示前5个外星人。
# for alien in aliens[:5]:
#     print(alien)
# print("-------------")
#
# # 显示创建了多少个外星人。
#
# print(len(aliens))


# 创建一个用于存储外星人的空列表。
aliens = []

# 创建30个绿色的外星人。
for alien_number in range (30):
    new_alien = {'color': 'yello', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "blue"
        alien["speed"] = "fast"
        alien["poiints"] = 22
    else:
        print("没有这个颜色的外星人")
print(alien)
# 显示前5个外星人。
for alien in aliens[:5]:
    print(alien)
print("...")


