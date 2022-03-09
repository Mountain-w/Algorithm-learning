from answers.decorator_helpers.timedecorators import time_helper


# 1.请同学们自行搜索或者想象一个象棋的棋盘，
# 然后把整个棋盘放入第一象限，棋盘的最左下角是（0，0）位置
# 那么整个棋盘就是横坐标上 9 条线，纵坐标上 10 条线的区域
# 给你三个参数 x，y，k
# 返回 马（马走日）从 （0，0）位置出发，必须走 k 步
# 最后落在（x，y）上的方法数有多少。
# 递归解

@time_helper
def findways(x, y, k):
    if x < 0 or x > 9 or y > 10 or y < 0 or k < 0:
        return -1
    print('递归解：')
    print(process_1(x, y, k, 0, 0))


def process_1(x, y, k, i, j):
    if k == 0:
        return 1 if i == x and j == y else 0
    ways = 0
    if i + 2 <= 9 and j + 1 <= 10:
        ways += process_1(x, y, k - 1, i + 2, j + 1)
    if i + 1 <= 9 and j + 2 <= 10:
        ways += process_1(x, y, k - 1, i + 1, j + 2)
    if i - 1 >= 0 and j - 2 >= 0:
        ways += process_1(x, y, k - 1, i - 1, j - 2)
    if i - 2 >= 0 and j - 1 >= 0:
        ways += process_1(x, y, k - 1, i - 2, j - 1)
    if i - 1 >= 0 and j + 2 <= 10:
        ways += process_1(x, y, k - 1, i - 1, j + 2)
    if i - 2 >= 0 and j + 1 <= 10:
        ways += process_1(x, y, k - 1, i - 2, j + 1)
    if i + 1 <= 9 and j - 2 >= 0:
        ways += process_1(x, y, k - 1, i + 1, j - 2)
    if i + 2 <= 9 and j - 1 >= 0:
        ways += process_1(x, y, k - 1, i + 2, j - 1)
    return ways


@time_helper
def findways_dp(x, y, k):
    if x < 0 or x > 9 or y > 10 or y < 0 or k < 0:
        return -1
    print('动态规划：')
    print(process_dp_1(x, y, k))


def process_dp_1(x, y, k):
    dp = [[[0] * 10 for _ in range(11)] for _ in range(k + 1)]
    dp[0][y][x] = 1
    for i in range(1, k + 1):
        for j in range(11):
            for h in range(10):
                ways = pick(dp, i - 1, j + 1, h + 2)
                ways += pick(dp, i - 1, j + 1, h - 2)
                ways += pick(dp, i - 1, j + 2, h - 1)
                ways += pick(dp, i - 1, j + 2, h + 1)
                ways += pick(dp, i - 1, j - 1, h + 2)
                ways += pick(dp, i - 1, j - 1, h - 2)
                ways += pick(dp, i - 1, j - 2, h + 1)
                ways += pick(dp, i - 1, j - 2, h - 1)
                dp[i][j][h] = ways

    return dp[k][0][0]


def pick(dp, k, y, x):
    if x < 0 or y > 10 or y < 0 or x > 9:
        return 0
    return dp[k][y][x]


if __name__ == '__main__':
    x = 7
    y = 7
    k = 9
    findways(x, y, k)
    findways_dp(x, y, k)
