# -*- coding: utf-8 -*-
import random
# nums=random.choices(range(1,7),k=5)
# print(nums)

# st="9451"
# li=[9,4,5,1]
# print(st[1],type(st[1]))
# print(li[3],type(li[3]))

# i=6
# pw="123456"
# g="124378"
# for a in range(i):
#     if int(pw[a]) == int(g[a]):
#         print("*",end=" ")
#     elif g[a] in pw:
#         print("+",end=" ")
#     else:
#         print("-",end=" ")

# i=6
# j=6
# pw=""
# nums = random.choices(range(1, j + 1), k=i)  # i:取i个数  j:在1~j-1的数中取
# for b in range(j):
#     pw = pw + str(nums[b])
#
# print(pw,type(pw))

import random
print("这是一个猜密码游戏")
dif=int(input("请选择难度:1.简单 2.普通 3.困难 4.自定义\n"))

#生成密码
def cr_pw(i,j):
    pw = ""
    nums = random.choices(range(1, j + 1), k=i)  # i:取i个数  j:在1~j-1的数中取
    for b in range(j):
        pw = pw + str(nums[b])
    return pw

#猜密码
def g_pw():
    g = input("请输入你猜的密码:")
    return g

#检查密码
def ch_pw(i):
    ch=""
    for a in range(i):
        if int(cr_pw(i,j)) == int(g_pw()):
            ch=ch+"*"
        elif g_pw()[a] in cr_pw():
            ch=ch+"+"
        else:
            ch=ch+"-"

#选择难度
if dif==1:
    print(cr_pw(6,6))
    if int(g_pw()) != int(cr_pw(6,6)):
        ch_pw()
        print("很遗憾,您没猜对,请根据线索重新判断")











