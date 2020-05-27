"""
problem 01.05 One Away

Description: 
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

Example 1:
Input: 
first = "pale"
second = "ple"
Output: True

Example 2:
Input: 
first = "pales"
second = "pal"
Output: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
"""

#use replace fucntion O(n)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) >= 2:
            return False
        if first == second:
            return True
        if len(first) == len(second):
            for i in range(len(first)):
                if first.replace(first[i], second[i], 1) == second:
                    return True
#change to swap so that fist is longer 
#		if len(first) < len(second):
#			first, second = second, first
        if len(first) < len(second):
            for char in second:
                if second.replace(char, '') == first.replace(char, ''):
                    return True
        if len(first) > len(second):
            for char in first:
                if first.replace(char, '') == second.replace(char, ''):
                    return True
        return False

#use counter and substring O(n)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        counter = 0
        if len(first) == len(second):
            for i in range(len(first)):
                if first[i] != second[i]:
                    counter += 1
                if counter > 1:
                    return False
            return True
#can replace the above return True with a condidtion: 
#		if first == second:
#			return True
        if len(first) < len(second):
            first, second = second, first
        for i in range(len(first)):
            if first[0:i] + first[i+1:] == second:
                return True
        return False
