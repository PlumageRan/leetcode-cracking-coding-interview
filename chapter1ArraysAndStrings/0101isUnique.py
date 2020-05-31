"""
problem 01.01 Is Unique

Description:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Example 1:
Input: s = "leetcode"
Output: false

Example 2:
Input: s = "abc"
Output: true
 
Note:
0 <= len(s) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
"""
#bitwise manipulation
class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord("a")
            if mark & (1 << move_bit) != 0:
                return False
            else: 
                mark |= (1 << move_bit)
        return True

#length of unique string
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len({*astr}) == len(astr)