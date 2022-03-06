# 给定一个 n，代表从 1 到 n 个格子，start 代表初始位置，问从初始位置走 k 步到 aim 处有几种方法
# 递归实现
def robot_1(n, start, aim, k):
    # 当步数用完了
    if k == 0:
        # 此时位置在目标处，说明是一种正确的走法，返回 1
        if start == aim:
            return 1
        # 此时位置不在目标处，也没有步数了，不是正确的走法，返回 0
        else:
            return 0
    ways = 0
    # 当走到 1 时，说明不能再往左走，只能往右走
    if start == 1:
        ways = robot_1(n, start + 1, aim, k - 1)
    # 当走到 n 时，说明不能再往右走，只能往左走
    elif start == n:
        ways = robot_1(n, start - 1, aim, k - 1)
    # 在中间的任意一个地方，都可以往左走或往右走，所以是两种走法的和。
    else:
        ways += robot_1(n, start + 1, aim, k - 1)
        ways += robot_1(n, start - 1, aim, k - 1)
    return ways


# 动态规划
def robot_dp(n, start, aim, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[aim][0] = 1
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            if i == 1:
                dp[i][j] = dp[i + 1][j - 1]
            elif i == n:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i + 1][j - 1]
    return dp[start][k]


print(robot_1(4, 2, 2, 2))
print(robot_dp(4, 2, 2, 2))


# 给定一个整数数组arr，代表数值不同的纸牌排成一条线
# 玩家 A 和玩家 B 依次拿走每张纸牌
# 规定玩家 A 先拿，玩家 B 后拿
# 但是每个玩家每次只能拿走最左或最右的纸牌
# 玩家 A 和 玩家 B 都绝顶聪明
# 请返回最后获胜者的分数

# 动态规划
def whowin_dp(arr):
    length = len(arr)
    f = [[0] * length for _ in range(length)]
    g = [[0] * length for _ in range(length)]
    for i in range(length):
        f[i][i] = arr[i]
    for j in range(length):
        g[j][j] = 0
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, length):
            f[i][j] = max(
                arr[i] + g[i + 1][j],
                arr[j] + g[i][j - 1]
            )
            g[i][j] = min(
                f[i + 1][j],
                f[i][j - 1]
            )
    return max(f[0][length - 1], g[0][length - 1])


# def whowin_dp(arr):
#     length = len(arr)
#     f = [[0] * length for _ in range(length)]
#     g = [[0] * length for _ in range(length)]
#     for i in range(length):
#         f[i][i] = arr[i]
#     for j in range(1, length):
#         l = 0
#         r = j
#         while r < length:
#             f[l][r] = max(
#                 arr[l] + g[l + 1][r],
#                 arr[r] + g[l][r - 1]
#             )
#             g[l][r] = min(
#                 f[l + 1][r],
#                 f[l][r - 1]
#             )
#             l += 1
#             r += 1
#     return max(
#         f[0][length - 1],
#         g[0][length - 1],
#     )

# 递归实现
def whowin(arr):
    f = first(arr, 0, len(arr) - 1)
    s = second(arr, 0, len(arr) - 1)
    return max(f, s)


def first(arr, l, r):
    if l == r:
        return arr[l]
    p1 = arr[l] + second(arr, l + 1, r)
    p2 = arr[r] + second(arr, l, r - 1)
    return max(p1, p2)


def second(arr, l, r):
    if l == r:
        return 0
    p1 = first(arr, l + 1, r)
    p2 = first(arr, l, r - 1)
    return min(p1, p2)


print(whowin([1, 100, 40, 60]))
print(whowin_dp([1, 100, 40, 60]))
