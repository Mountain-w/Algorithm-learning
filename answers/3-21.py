# 给定三个参数 N M K
# 怪兽有 N 滴血， 等着英雄砍自己
# 英雄每一次打击，都会让怪兽流失 [0 ~ M] 滴血
# 每一次打击等概率掉血
# 求 K 次打击之后，英雄把怪兽砍死的概率
from answers.decorator_helpers.timedecorators import time_helper


# 递归解法
@time_helper
def win(hp, hint, times):
    if hp < 0 or times < 0 or hint < 0:
        return 0
    print('递归解：')
    ways = process(hp, hint, times)
    print(ways, ways / pow(times, hint + 1))


def process(hp, hint, times):
    if times == 0:
        return 1 if hp <= 0 else 0
    ways = 0
    for hert in range(hint + 1):
        ways += process(hp - hert, hint, times - 1)
    return ways


@time_helper
def win_dp(hp, hint, times):
    print('动态规划：')
    dp = [[0] * (hp + 1) for _ in range(times + 1)]
    dp[0][0] = 1
    for i in range(1, times + 1):
        dp[i][0] = pow(hint + 1, i)
        for j in range(1, hp + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            if j - hint - 1 > 0:
                dp[i][j] -= dp[i - 1][j - hint - 1]
            else:
                dp[i][j] -= pow(hint + 1, i - 1)
    print(dp[times][hp])


# ******************************************************************************************
# arr 是面值数组，其中的指都是正数且没有重复，给定一个正数 aim
# 每个值都认为是一种面值，且认为张数是无限的
# 返回组成 aim 的最少货币数


# 递归解
@time_helper
def min_count(arr, aim):
    if not arr or aim <= 0:
        return 0
    print('递归解：')
    print(process_1(arr, aim, 0))


def process_1(arr, aim, index):
    if index == len(arr):
        return 0 if aim == 0 else float('inf')
    z = 0
    ans = float('inf')
    while arr[index] * z <= aim:
        next = process_1(arr, aim - arr[index] * z, index + 1)
        if next != float('inf'):
            ans = min(ans, z + next)
        z += 1
    return ans


@time_helper
def min_dp(arr, aim):
    print('动态规划：')
    length = len(arr)
    dp = [[0] * (aim + 1) for _ in range(length + 1)]
    for k in range(1, aim + 1):
        dp[length][k] = float('inf')
    dp[length][0] = 0
    for i in range(length - 1, -1, -1):

        for j in range(aim + 1):
            z = 0
            ans = float('inf')
            while arr[i] * z <= j:
                next = dp[i + 1][j - arr[i] * z]
                if next != float('inf'):
                    ans = min(ans, z + dp[i + 1][j - arr[i] * z])
                z += 1
            dp[i][j] = ans
    print(dp[0][aim])


@time_helper
def min_dp2(arr, aim):
    print('动态规划2：')
    length = len(arr)
    dp = [[0] * (aim + 1) for _ in range(length + 1)]
    for k in range(1, aim + 1):
        dp[length][k] = float('inf')
    dp[length][0] = 0
    for i in range(length - 1, -1, -1):
        for j in range(aim + 1):
            dp[i][j] = dp[i + 1][j]
            if j - arr[i] >= 0 and dp[i][j - arr[i]] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i][j - arr[i]] + 1)

    print(dp[0][aim])


if __name__ == '__main__':
    print('*' * 9, '第一题', '*' * 9)
    hp = 20
    hint = 4
    times = 8
    win(hp, hint, times)
    win_dp(hp, hint, times)
    print('*' * 9, '第二题', '*' * 9)
    arr = [24, 2, 18, 1]
    aim = 300
    min_count(arr, aim)
    min_dp(arr, aim)
    min_dp2(arr, aim)
