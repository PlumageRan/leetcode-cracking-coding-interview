"""
problem 02.02 Kth Node From End of List

Description:
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:
Input:  1->2->3->4->5 and k = 2
Output:  4

Note:
k is always valid.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
"""

#brute force O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if not head:
            return None
        pre, cur = head, head.next
        count = 1
        while cur:
            count += 1
            pre, cur = cur, cur.next
        pre, cur = head, head.next
        while count != k:
            count -= 1
            pre, cur = cur, cur.next
        return pre.val

#two pointers O(n)
#let fast pointer go k times first and then let slow pointer go, when fast pointer arrives the end, slow pointer is at Kth to the end
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val