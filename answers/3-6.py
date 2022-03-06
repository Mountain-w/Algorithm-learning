# 1.给定两个数组 v, w。v 数组每一个元素代表货物的价值，w 数组每一个元素代表货物的价值，给定一个 bag，代表最多能放多大质量的货物
# 问：在不超过 bag 的情况下，能获得的最大价值是多少。（所有货物自由选择）
print('*' * 20)


def maxvalue(w, v, bag):
    # 处理边界情况，如果不存在 w，v 或两个数组长度不相等，返回 0
    if not w or not v or len(w) != len(v):
        return 0
    print('递归解： ', process(w, v, bag, 0))
    print('动态规划解： ', process_dp(w, v, bag))


# 递归实现


def process(w, v, rest, index):
    # 如果背包容量小于 0 了，说明前一步做的决策是错误的，返回 -1
    if rest < 0:
        return -1
    # 到了数组的末尾了,没有货了
    if index == len(w):
        return 0
    # 不要当前的货物
    p1 = process(w, v, rest, index + 1)
    # 要当前的货物
    p2 = float('-inf')
    next = process(w, v, rest - w[index], index + 1)
    # 要当前货物是否是正确的决策，如果为 -1 说明是无效的决策
    if next != -1:
        # 是有效的，就让当前货物价值加上后续过程获得的价值
        p2 = v[index] + next
    # 因为求最大，所以返回两种决策的最大值
    return max(p1, p2)


# def process1(w, v, rest, index):
#     # 到了数组的末尾了,没有货了
#     if index == len(w):
#         return 0
#     # 不要当前的货物
#     p1 = process(w, v, rest, index + 1)
#     # 要当前的货物
#     p2 = float('-inf')
#     # 如果还能装下当前货物
#     if rest - w[index] >= 0:
#         p2 = v[index] + process1(w, v, rest-w[index], index+1)
#     # 因为求最大，所以返回两种决策的最大值
#     return max(p1, p2)

# 动态规划


def process_dp(w, v, bag):
    length = len(w)
    dp = [[0] * (bag + 1) for _ in range(length + 1)]
    for i in range(length - 1, -1, -1):
        for j in range(bag + 1):
            dp[i][j] = dp[i + 1][j]
            if j - w[i] >= 0:
                dp[i][j] = max(dp[i + 1][j], v[i] + dp[i + 1][j - w[i]])

    return dp[0][bag]


w = [3, 7, 10, 8]
v = [3, 8, 23, 20]
bag = 15
maxvalue(w, v, bag)

# 2.规定 1 和 A 对应， 2 和 B 对应， 3 和 C 对应，... ... 26 和 Z 对应
# 那么一个数字字符串，比如 ‘111’ 就可以转化成：
# AAA，KA，AK 三种字符串
# 给定一个只有数字字符组成的字符串，返回有多少种转化结果。
print("*" * 20)


def number_to_str(number):
    if not number:
        return 0
    print('递归实现： ', process2(number, 0))
    print('动态规划解： ', process2_dp(number))


# 递归实现
def process2(number, index):
    # 表示来到了末尾，没有一个数字没转化，是正确的决策，返回 1
    if index == len(number):
        return 1
    # 单个 0 不能被转化，所以返回 0
    if number[index] == '0':
        return 0
    # 第一种情况：只转化当前的数字
    ways = process2(number, index + 1)
    # 第二种情况：如果下一个数字和当前的数字组合能转化，一起转化
    # 当前数字不能是最后一个，当前数字和下一个数字组合得到的数字小于 27
    if index + 1 < len(number) and int(number[index:index + 2]) < 27:
        ways += process2(number, index + 2)
    return ways


# 动态规划
def process2_dp(number):
    length = len(number)
    dp = [0] * (length + 1)
    dp[length] = 1
    for i in range(length - 1, -1, -1):
        if number[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < length and int(number[i:i + 2]) < 27:
                dp[i] += dp[i + 2]
    return dp[0]


number = '305'
number_to_str(number)
