# 1.给出一个可能包含重复的整数数组，和一个大小为 k 的滑动窗口, 从左到右在数组中滑动这个窗口，找到数组中每个窗口内的最大值。
# lintcode原题链接：https://www.lintcode.com/problem/362/


from typing import (
    List,
)


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        # write your code here
        if not nums:
            return []
        from collections import deque
        windows = deque()
        result = []
        for i in range(len(nums)):
            # 更新单调队列
            while windows and nums[i] >= nums[windows[-1]]:
                windows.pop()
            windows.append(i)
            # 窗口未形成
            if i < k - 1:
                continue
            # 窗口已经形成
            # 添加此时最大值
            result.append(nums[windows[0]])
            if windows[0] == i - k + 1:
                windows.popleft()
        return result

# 2. 给定一个整型数组 arr，和一个整数 num
# 某个 arr 中的子数组 sub，如果想达标，必须满足：
# sub 中最大值 - sub 中最小值 <= num，
# 返回 arr 中达标子数组的数量
