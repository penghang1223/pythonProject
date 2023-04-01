while True:
    try:
        n=int(input()) #读入第一行：随机整数的个数
        res=set()


        for i in range(n):
            res.add(int(input()))# 读入第n行：n个随机整数组成的数组
            # 打印集合res
        for i in sorted(res):
            print(i)
    except:
        break