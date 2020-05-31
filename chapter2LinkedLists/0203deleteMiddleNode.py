"""
problem 02.03 Delete Middle Node

Description:
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

 

Example:

Input: the node c from the linked list a->b->c->d->e->f
Output: nothing is returned, but the new linked list looks like a->b->d->e->f

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-middle-node-lcci
"""

#let node's value equal to next node's value, and next node's access equal to next next node's access
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
