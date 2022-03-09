from answers.decorator_helpers.timedecorators import time_helper


# 1.给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/qJnOS7

# 递归解
@time_helper
def longestCommonSubsequence_1(text1: str, text2: str) -> int:
    if not text1 or not text2:
        return 0
    print('递归解：')
    process_1(text1, text2, len(text1) - 1, len(text2) - 1)


def process_1(text1, text2, i, j):
    if i == 0 and j == 0:
        return 1 if text1[i] == text2[j] else 0
    elif i == 0:
        if text1[i] == text2[j]:
            return 1
        else:
            return process_1(text1, text2, i, j - 1)
    elif j == 0:
        if text1[i] == text2[j]:
            return 1
        else:
            return process_1(text1, text2, i - 1, j)
    else:
        # i, j 都不为 0
        # 第一种情况，可能要 i，不要 j
        p1 = process_1(text1, text2, i, j - 1)
        # 第二种情况，可能要 j，不要 i
        p2 = process_1(text1, text2, i - 1, j)
        # 第三种情况，两个都要，但是必须 text1[i] == text2[j]
        p3 = 1 + process_1(text1, text2, i - 1, j - 1) if text1[i] == text2[j] else float('-inf')
        # 取最大值
        return max(p1, max(p2, p3))


# 动态规划解
@time_helper
def longestCommonSubsequence_2(text1, text2):
    if not text1 or not text2:
        return 0
    print("动态规划：")
    process_1_dp(text1, text2)


def process_1_dp(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if text1[0] == text2[0] else 0
    for i in range(1, n):
        dp[0][i] = 1 if text1[0] == text2[i] else dp[0][i - 1]
    for j in range(1, m):
        dp[j][0] = 1 if text1[j] == text2[0] else dp[j - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            p1 = dp[i - 1][j]
            p2 = dp[i][j - 1]
            p3 = 1 + dp[i - 1][j - 1] if text1[i] == text2[j] else float('-inf')
            dp[i][j] = max(p1, max(p2, p3))
    return dp[m - 1][n - 1]


# --------------------------------------------分界线-----------------------------------------------------
# 2.给定一个字符串 string，返回这个字符串的最长回文子序列长度
# 比如：string = 'a12b3c43def2ghi1kpm'
# 最长回文子序列是 '1234321' or '123c321'，返回长度 7
# 递归
@time_helper
def longest_palindrome_subseq1(string: str) -> int:
    if not string:
        return 0
    print("递归解法1：")
    print(process_2(string, 0, len(string) - 1))


def process_2(string, i, j):
    if i == j:
        return 1
    if i == j - 1:
        return 2 if string[i] == string[j] else 1
    p1 = process_2(string, i, j - 1)
    p2 = process_2(string, i + 1, j)
    p3 = process_2(string, i + 1, j - 1) + 2 if string[i] == string[j] else float('-inf')
    p4 = process_2(string, i + 1, j - 1)
    return max(max(p1, p2), max(p3, p4))


@time_helper
def longest_palindrome_subseq2(string: str) -> int:
    if not string:
        return 0
    print("递归解法2：")
    print(process_2_2(string, 0, len(string) - 1))


def process_2_2(string, i, j):
    if i == j:
        return 1
    if i == j - 1:
        return 2 if string[i] == string[j] else 1
    p1 = process_2(string, i, j - 1)
    p2 = process_2(string, i + 1, j)
    p3 = process_2(string, i + 1, j - 1) + 2 if string[i] == string[j] else float('-inf')
    return max(p1, max(p2, p3))

# 动态规划
@time_helper
def longest_palindrome_subseq_dp_1(string: str) -> int:
    if not string:
        return 0
    print("动态规划1：")
    print(process_2_dp(string))


@time_helper
def longest_palindrome_subseq_dp_2(string: str) -> int:
    if not string:
        return 0
    print("动态规划2：")
    print(process_2_dp_2(string))


# 动态规划1：

def process_2_dp(string):
    m = len(string)
    dp = [[0] * m for _ in range(m)]
    dp[m - 1][m - 1] = 1
    for i in range(m - 1):
        dp[i][i] = 1
        dp[i][i + 1] = 2 if string[i] == string[i + 1] else 1
    for i in range(m - 3, -1, -1):
        for j in range(i + 2, m):
            p1 = dp[i][j - 1]
            p2 = dp[i + 1][j]
            p3 = (2 + dp[i + 1][j - 1]) if string[i] == string[j] else float('-inf')
            p4 = dp[i + 1][j - 1]
            dp[i][j] = max(max(p1, p2), max(p3, p4))
    return dp[0][m - 1]


# 动态规划2：

def process_2_dp_2(string):
    m = len(string)
    dp = [[0] * m for _ in range(m)]
    dp[m - 1][m - 1] = 1
    for i in range(m - 1):
        dp[i][i] = 1
        dp[i][i + 1] = 2 if string[i] == string[i + 1] else 1
    for i in range(m - 3, -1, -1):
        for j in range(i + 2, m):
            p1 = dp[i][j - 1]
            p2 = dp[i + 1][j]
            dp[i][j] = max(p1, p2)
            if string[i] == string[j]:
                p3 = (2 + dp[i + 1][j - 1])
                dp[i][j] = max(p1, max(p2, p3))
    return dp[0][m - 1]


if __name__ == "__main__":
    print('*' * 9, '第一题', '*' * 9)
    text1 = 'abc2de'
    text2 = 'a1b2d3e'
    longestCommonSubsequence_1(text1, text2)
    longestCommonSubsequence_2(text1, text2)
    print('*' * 9, '第二题', '*' * 9)
    string = 'a12b3c43def2ghi1kpm'
    longest_palindrome_subseq1(string)
    longest_palindrome_subseq2(string)
    longest_palindrome_subseq_dp_1(string)
    longest_palindrome_subseq_dp_2(string)
