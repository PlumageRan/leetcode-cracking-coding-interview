"""
problem 01.09 String Rotation

Description:
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 (e.g.,"waterbottle" is a rotation of"erbottlewat"). Can you use only one call to the method that checks if one word is a substring of another?

Example 1:
Input: s1 = "waterbottle", s2 = "erbottlewat"
Output: True

Example 2:
Input: s1 = "aa", "aba"
Output: False
 
Note:
0 <= s1.length, s1.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-rotation-lcci
"""
#python string operation O(n)
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> str:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        for i in range(len(s1)):
            if s1[i:]+s1[:i] == s2:
                return True
        return False