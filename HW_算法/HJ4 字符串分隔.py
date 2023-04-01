# 多行输入时抛出异常


while True:
    try:
        s = input()
        while len(s)>8:
            print(s[:8])   #打印前八个字符串
            s=s[8:]  #从第八个切片
        print(s.ljust(8,"0"))  #8是宽度  0 是在不满足8长度时 在末尾补上0

        # ljust(width) & rjust(width) & center(width)
    except:
        break