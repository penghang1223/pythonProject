# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
while True:
    try:
        s = input()
        print(int(s,16))
        # int类型可以直接进行进制转换
    except:
        break