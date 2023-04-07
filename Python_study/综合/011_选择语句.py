age = int(input("输入你的年纪:"))

if age > 18:
    print("你的年龄大于18")
elif age < 18:
    print("你的年龄小于18")
elif 20 < age < 30:
    print("你的年龄大于20小于30")
else:
    print("你太老了")
