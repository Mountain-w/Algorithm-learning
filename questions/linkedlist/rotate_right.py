# 描述
# 给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数
# 样例
# 样例 1:
# 输入：1->2->3->4->5  k = 2
# 输出：4->5->1->2->3
# 样例 2:
# 输入：3->2->1  k = 1
# 输出：1->3->2
# 原题链接：https://www.lintcode.com/problem/170/description
from questions.datastruct.ListNode import ListNode


def get_length_tail(head):
    tail = head
    length = 1
    while tail.next:
        length += 1
        tail = tail.next
    return length, tail


# 解法1：

# 旋转链表k步可以转换成将倒数第 k 个节点作为新链表的头部
def rotate_right1(head: ListNode, k):
    if head is None:
        return None
    # 获取链表长度和尾部：
    length, tail = get_length_tail(head)
    # 如果 k 是链表长度的整倍数，就不用反转，或者链表只有一个节点。
    if k % length == 0 or length == 1:
        return head
    # 将链表头尾相接，生成新链表时就不会断
    tail.next = head
    # 找到倒数第 k-1 个节点
    count = length - k % length - 1
    cur = head
    while count > 0:
        count -= 1
        cur = cur.next
    # cur 为倒数第 k - 1个节点，所以cur为新尾部，cur.next 为新头部
    newhead = cur.next
    cur.next = None
    return newhead


# 解法二：

# 快慢指针
def rotate_right2(head: ListNode, k):
    if head is None:
        return None
    length, _ = get_length_tail(head)
    if k % length == 0 or head.next is None:
        return head
    # 定义快慢指针
    fast = head
    low = head
    # fast 指针先走k步
    for _ in range(k):
        if fast.next:
            fast = fast.next
    # fast, low 一起走
    while fast.next:
        fast = fast.next
        low = low.next
    # fast 来到链表尾部
    fast.next = head
    newhead = low.next
    low.next = None
    return newhead
