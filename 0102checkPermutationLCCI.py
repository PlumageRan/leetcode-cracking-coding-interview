"""
problem 01.02 Check Permutation LCCI
description
Given two strings,write a method to decide if one is a permutation of the other.

Example 1:
Input: s1 = "abc", s2 = "bca"
Output: true

Example 2:
Input: s1 = "abc", s2 = "bad"
Output: false

Note:
0 <= len(s1) <= 100
0 <= len(s2) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
"""
#hash: O(n)
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        counter = [0] * 26
        for char in s1:
            counter[ord(char)-ord("a")-1] += 1
        for char in s2:
            counter[ord(char)-ord("a")-1] -= 1
        for ele in counter:
            if ele == 0:
                continue
            else:
                return False
        return True
#sort: O(nlogn)
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

