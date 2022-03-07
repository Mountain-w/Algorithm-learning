# 1.给定两个数组 v, w。v 数组每一个元素代表货物的价值，w 数组每一个元素代表货物的价值，给定一个 bag，代表最多能放多大质量的货物
# 问：在不超过 bag 的情况下，能获得的最大价值是多少。（所有货物自由选择）


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


# 2.规定 1 和 A 对应， 2 和 B 对应， 3 和 C 对应，... ... 26 和 Z 对应
# 那么一个数字字符串，比如 ‘111’ 就可以转化成：
# AAA，KA，AK 三种字符串
# 给定一个只有数字字符组成的字符串，返回有多少种转化结果。
# print("*" * 20)


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
        if number[i] != '0':
            dp[i] = dp[i + 1]
            if i + 1 < length and int(number[i:i + 2]) < 27:
                dp[i] += dp[i + 2]
    return dp[0]


# 3.给定一个字符串 string，给定一个字符串类型的数组 arr，出现的字符都是小写英文
# arr 每一个字符串，代表一张贴纸，你可以把单个字符剪开来使用，目的是拼出 string
# 问：至少多少张贴纸可以完成这个任务（每个贴纸无数张）
# 例子：
# string = "babac"
# arr = ['ba', 'c', 'abcd']
# 至少需要两张贴纸 "ba" 和 "abcd"。
# 力扣原题：https://leetcode-cn.com/problems/stickers-to-spell-word/submissions/
# 用解法三直接跑过，最优解
# 解法 1
def splicing_1(arr, string):
    value = process_splicing_1(arr, string)
    return 0 if value == float('inf') else value


def minus(s1, s2):
    a = ord('a')
    count = [0] * 27
    result = []
    for i in s1:
        count[ord(i) - a] += 1
    for j in s2:
        count[ord(j) - a] -= 1
    for i in range(26):
        if count[i] > 0:
            for _ in range(count[i]):
                result.append(chr(i + a))
    return ''.join(result)


# 递归实现
def process_splicing_1(arr, string):
    if len(string) == 0:
        return 0
    _min = float('inf')
    for first in arr:
        rest = minus(string, first)
        if len(rest) != len(string):
            _min = min(_min, process_splicing_1(arr, rest))
    return _min + (0 if _min == float('inf') else 1)


# 解法二
def splicing_2(arr, string):
    # 生成每一个贴纸的词频统计
    arr = word_count(arr)
    # 开始递归
    return process_splicing_2(arr, string)


def process_splicing_2(arr, string):
    if len(string) == 0:
        return 0
    # 生成 string 的词频
    a = ord('a')
    count = [0] * 26
    _min = float('inf')
    for s in string:
        count[ord(s) - a] += 1
    for k in arr:
        if k[ord(string[0]) - a] > 0:
            target = []
            for i in range(26):
                if count[i] > 0:
                    num = count[i] - k[i]
                    if num > 0:
                        for _ in range(num):
                            target.append(chr(i+a))
            _min = min(_min, process_splicing_2(arr, ''.join(target)))
    return _min + (0 if _min == float('inf') else 1)


def word_count(arr):
    result = []
    a = ord('a')
    for string in arr:
        count = [0] * 26
        for j in string:
            count[ord(j) - a] += 1
        result.append(count)
    return result


# 解法三(记忆化搜索)
def splicing_3(arr, string):
    # 这道题没有严格表依赖，所以用记忆化搜索，建立一个字典存储中间结果。
    dp = {}
    # 生成每一个贴纸的词频统计
    arr = word_count(arr)
    # 开始递归
    return process_splicing_3(arr, string, dp)


def process_splicing_3(arr, string, dp):
    # 如果结果在字典中，直接返回
    if dp.get(string, None):
        return dp[string]
    if len(string) == 0:
        return 0
    # 生成 string 的词频
    a = ord('a')
    count = [0] * 26
    _min = float('inf')
    for s in string:
        count[ord(s) - a] += 1

    for k in arr:
        # 剪枝：将不含有以 string 第一个字符的贴纸跳过。
        # ord(string[0]-a) 找到 string 第一个字符的 ascii
        # k[ord(string[0]-1] 查看贴纸对应字符数
        # 如果大于 0，说明含有 string 第一个字符。
        if k[ord(string[0]) - a] > 0:
            target = []
            for i in range(26):
                # 将 string 的字符出现的次数减去贴纸中对应的次数
                if count[i] > 0:
                    num = count[i] - k[i]
                    # 重新生成 string
                    for _ in range(num):
                        target.append(chr(i + a))
            # 进行下一次递归
            _min = min(_min, process_splicing_3(arr, ''.join(target), dp))
    ans = _min + (0 if _min == float('inf') else 1)
    # 将结果存到字典中
    dp[string] = ans
    return ans


if __name__ == "__main__":
    print('*' * 9, "第一题", "*" * 9)
    w = [3, 7, 10, 8]
    v = [3, 8, 23, 20]
    bag = 15
    maxvalue(w, v, bag)
    print('*' * 9, "第二题", "*" * 9)
    number = '111'
    number_to_str(number)
    print('*' * 9, "第三题", "*" * 9)
    arr = ["these", "guess", "about", "garden", "him"]
    string = "atomher"
    print('解法1：', splicing_1(arr, string))
    print('解法2：', splicing_2(arr, string))
    print('解法3：', splicing_3(arr, string))
