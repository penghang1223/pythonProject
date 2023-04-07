# print("今有物不知其数，三三数之剩二；五五数之剩三，七七数之剩二；问物几何？")
# none = True
# number = 0
# while none:
#     number +=1
#     if number%3 == 2 and number%5==3 and number%7 ==2:
#         print(f"这个数是:{number}")
#         none = False
#

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car =="bmw":
#         print("这是宝马")
#     elif car =="toyota":
#         print("这是toyouta")
#     else:
#         print(car)

#
# alien_color = "red"
# if alien_color == "green":
#     print("外星人是绿的")
#     print("你获得5分")
# else:
#     print("10分")

#
# fruit_list = ["apple","bananas","orange"]
# if 'apple' in fruit_list:
#     print("You really like apple!")
# if "bananas" in fruit_list:
#     print("You really like bananas!")

#
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
# else:
#     print(f"Adding {requested_topping}.")
#
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#     print(type(requested_toppings))
# else:
#     print("没了")


# 列表比较


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
