"""
problem 01.03 String to URL

Description:
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

Example 1:
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

Example 2:
Input: "               ", 5
Output: "%20%20%20%20%20"
 

Note:
0 <= S.length <= 500000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-url-lcci
"""

#use additional space O(n)
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        result = ""
        for i in range(length):
            if S[i] == " ":
                result += "%20"
            else:
                result += S[i]
        return result

#use replace function O(n)
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[0: length].replace(" ", "%20")