"""
problem 01.04 Palindrome Permutation

Description:
Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

Example1:
Input: "tactcoa"
Output: true（permutations: "tacocat"、"atcocta", etc.）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
"""
#use counter O(n)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = [0] * 52
        mark = 0
        for char in s:
            counter[ord(char)-ord("a")] += 1
        for num in counter:
            if num % 2 == 1:
                mark += 1
            if mark >= 2:
                return False
        return True

#use stack O(n)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cur = []
        res = 0
        for char in s:
            if char in cur:
                cur.remove(char)
                res -= 1
            else:
                cur.append(char)
                res += 1
        if res <= 1:
            return True
        else: 
            return False