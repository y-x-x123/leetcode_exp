'''
输入：
1
2 3
输出：
['1', '2', '3']
'''
# import sys
# data = sys.stdin.read().strip().split() # mac上control + D 代表输入结束 win上 ctrl +z 再按回车
# print(data) # 返回列表

# input = sys.stdin.readline
# T = int(input())
# ans = []
# for _ in range(T):
#     a, b = map(int, input().split())
#     ans.append(str(a + b))
# print('\n'.join(ans))


# -------变成json格式的-----
# import sys
# import json
# s = sys.stdin.read().strip()
# d = json.loads(s)
# print(d)


# ---- map和input------
# a,b = map(int, input().split())
# print(a + b)


# --------
# 输入
# 3
# 1 2
# 10 20
# 100 200
# 输出
# 3
# 30
# 300

# t = int(input())
# for _ in range(t):
#     a,b = map(int, input().split())
#     print(a + b)



# import sys
# data = sys.stdin.read().strip().split()  # 转化成了列表
# print(data)
# print(type(data))
# print(len(data))

# data = list(map(int,input().split())) # 转化成了列表
# print(data)


import sys

for line in sys.stdin:
    print(type(line))