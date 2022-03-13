from answers.decorator_helpers.timedecorators import time_helper


# 1.给定一个二维数组matrix，一个人必须从左上角出发，最后到达右下角
# 沿途只可以向下或者向右走，沿途的数字都累加就是距离的累加和
# 返回最小距离累加和

# 递归解

@time_helper
def min_d(matrix):
    if not matrix:
        return 0
    h = len(matrix)
    l = len(matrix[0])
    print('递归解：')
    print(process1(matrix, 0, 0, l, h))


def process1(matrix, x, y, l, h):
    if x == l - 1 and y == h - 1:
        return matrix[y][x]
    p1 = float('inf')
    p2 = float('inf')
    # 向右走
    if x < l - 1:
        p1 = matrix[y][x] + process1(matrix, x + 1, y, l, h)
    # 向下走
    if y < h - 1:
        p2 = matrix[y][x] + process1(matrix, x, y + 1, l, h)
    return min(p1, p2)


# 动态规划1
@time_helper
def min_d_dp_1(matrix):
    if not matrix:
        return 0
    l = len(matrix[0])
    h = len(matrix)
    print('动态规划1：')
    dp = [[0] * l for _ in range(h)]
    dp[h - 1][l - 1] = matrix[h - 1][l - 1]
    for i in range(h - 2, -1, -1):
        dp[i][l - 1] = matrix[i][l - 1] + dp[i + 1][l - 1]
    for j in range(l - 2, -1, -1):
        dp[h - 1][j] = matrix[h - 1][j] + dp[h - 1][j + 1]
    for i in range(h - 2, -1, -1):
        for j in range(l - 2, -1, -1):
            p1 = matrix[i][j] + dp[i + 1][j]
            p2 = matrix[i][j] + dp[i][j + 1]
            dp[i][j] = min(p1, p2)
    print(dp[0][0])


# 动态规划2（空间压缩行）
@time_helper
def min_d_dp_2(matrix):
    if not matrix:
        return 0
    l = len(matrix[0])
    h = len(matrix)
    print('动态规划2：')
    dp = [0] * l
    dp[l - 1] = matrix[h - 1][l - 1]
    for i in range(l - 2, -1, -1):
        dp[i] = matrix[h - 1][i] + dp[i + 1]
    for j in range(h - 2, -1, -1):
        dp[l - 1] += matrix[j][l - 1]
        for k in range(l - 2, -1, -1):
            p1 = dp[k]
            p2 = dp[k + 1]
            dp[k] = matrix[j][k] + min(p1, p2)
    print(dp[0])


# 动态规划3（空间压缩列）
@time_helper
def min_d_dp_3(matrix):
    if not matrix:
        return 0
    l = len(matrix[0])
    h = len(matrix)
    print('动态规划3：')
    dp = [0] * h
    dp[h - 1] = matrix[h - 1][l - 1]
    for i in range(h - 2, -1, -1):
        dp[i] = matrix[i][l - 1] + dp[i + 1]
    for j in range(l - 2, -1, -1):
        dp[h - 1] += matrix[h - 1][j]
        for k in range(h - 2, -1, -1):
            p1 = dp[k]
            p2 = dp[k + 1]
            dp[k] = matrix[k][j] + min(p1, p2)
    print(dp[0])


if __name__ == '__main__':
    matrix = [
        [2, 3, 1, 5, 3],
        [5, 3, 9, 10, 3],
        [3, 1, 0, 1, 4],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 10, 1],
        [0, 0, 1, 1, 10],
        [0, 0, 1, 1, 20],
    ]
    min_d(matrix)
    min_d_dp_1(matrix)
    min_d_dp_2(matrix)
    min_d_dp_3(matrix)

# ----------------------------------分割线---------------------------------------
# 2.arr是货币数组，其中的值都是正数。再给定一个正数aim。
# 每个值都认为是一张货币，
# 即便是值相同的货币也认为每一张是不同的，
# 返回组成aim的方法数
# 例如： arr = [1, 1, 1], aim = 2
# 第0个和第一个能组成2，第1个和第2个能组成2，第0个和第2个能组成2
# 一共就三种方法，所以返回3
