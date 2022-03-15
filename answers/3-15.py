from answers.decorator_helpers.timedecorators import time_helper


# 1. arr 是面值数组，其中的值都是正数且没有重复。再给定一个正数 aim。
# 每个值都认为是一种面值，且认为张数无限
# 返回组成 aim 的方法数
# 例如： arr[1, 2], aim = 4
# 方法如下： 1 + 1 + 1 + 1， 1 + 1 + 2， 2 + 2
# 一共就三种方法。

@time_helper
def findways(arr, aim):
    if not arr or aim < 0:
        return 0
    print('递归解：')
    print(process1(arr, aim, 0))


def process1(arr, aim, i):
    if i == len(arr):
        return 1 if aim == 0 else 0
    z = 0
    ways = 0
    while aim - z * arr[i] >= 0:
        ways += process1(arr, aim - z * arr[i], i + 1)
        z += 1
    return ways


@time_helper
def findways_dp(arr, aim):
    print("动态规划：")
    length = len(arr)
    dp = [[0] * (aim + 1) for _ in range(length + 1)]
    dp[length][0] = 1
    for i in range(length - 1, -1, -1):
        for j in range(aim + 1):
            z = 0
            while j - z * arr[i] >= 0:
                dp[i][j] += dp[i + 1][j - z * arr[i]]
                z += 1
    print(dp[0][aim])


@time_helper
def findways_dp_1(arr, aim):
    print("动态规划(优化)：")
    length = len(arr)
    dp = [[0] * (aim + 1) for _ in range(length + 1)]
    dp[length][0] = 1
    for i in range(length - 1, -1, -1):
        for j in range(aim + 1):
            dp[i][j] = dp[i + 1][j]
            if j - arr[i] >= 0:
                dp[i][j] += dp[i][j - arr[i]]
    print(dp[0][aim])


# 2. arr 是面值数组，其中的值都是正数且没有重复。再给定一个正数 aim。
# 每个值都认为是一种面值，给定一个张数数组 counts，代表每个面值能用多少次
# 返回组成 aim 的方法数
# 例如： arr[1, 2], aim = 4, counts = [1, 2]
# 方法如下： 2 + 2 = 4
# 一共就一种方法。
@time_helper
def findways_limit(arr, counts, aim):
    if not arr or aim < 0 or len(arr) != len(counts):
        return 0
    print('递归解：')
    print(process2(arr, counts, aim, 0))


def process2(arr, counts, aim, index):
    if index == len(arr):
        return 1 if aim == 0 else 0
    ways = 0
    for i in range(counts[index]+1):
        if aim - i * arr[index] >= 0:
            ways += process2(arr, counts, aim - i * arr[index], index + 1)
    return ways


@time_helper
def findways_limit_dp(arr, counts, aim):
    print('动态规划：')
    length = len(arr)
    dp = [[0] * (aim+1) for _ in range(length+1)]
    dp[length][0] = 1
    for i in range(length-1, -1, -1):
        for j in range(aim+1):
            for k in range(counts[i]+1):
                if j - k * arr[i] >= 0:
                    dp[i][j] += dp[i+1][j-k*arr[i]]
    print(dp[0][aim])


@time_helper
def findways_limit_dp_2(arr, counts, aim):
    print('动态规划(优化)：')
    length = len(arr)
    dp = [[0] * (aim+1) for _ in range(length+1)]
    dp[length][0] = 1
    for i in range(length-1, -1, -1):
        for j in range(aim+1):
            dp[i][j] = dp[i+1][j]
            if j - (counts[i]+1)*arr[i] >= 0:
                dp[i][j] += dp[i][j-arr[i]] - dp[i+1][j - (counts[i]+1)*arr[i]]
            else:
                dp[i][j] += dp[i][j-arr[i]]
    print(dp[0][aim])


if __name__ == '__main__':
    print('*' * 9, '第一题', '*' * 9)
    arr = [1, 2, 5, 10, 100]
    aim = 201
    findways(arr, aim)
    findways_dp(arr, aim)
    findways_dp_1(arr, aim)
    print('*' * 9, '第二题', '*' * 9)
    arr = [1, 2, 4, 10]
    counts = [1, 20, 21, 2]
    aim = 90
    findways_limit(arr, counts, aim)
    findways_limit_dp(arr, counts, aim)
    findways_limit_dp_2(arr, counts, aim)
