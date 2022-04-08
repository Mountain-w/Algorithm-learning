from answers.decorator_helpers.timedecorators import time_helper


# 整数拆分问题，给定一个整数 n，将这个数拆分成几个数相加的形式，整体不能出现降序。
# 问：有多少方法数？
# 例子：3
# 拆分成 （1 + 2），（3），（1 + 1 + 1)
# 3种方法

# 递归方法
@time_helper
def find_ways(n):
    if n == 1:
        return 1
    result = []
    path = []
    print(process(result, path, n, 1))
    print(result)


def process(result, path, n, pre):
    if n == 0:
        result.append(path[:])
        return 1
    if pre > n:
        return 0
    ways = 0
    for i in range(pre, n+1):
        path.append(i)
        ways += process(result, path, n-i, i)
        path.pop()
    return ways


if __name__ == '__main__':
    n = 5
    find_ways(n)
