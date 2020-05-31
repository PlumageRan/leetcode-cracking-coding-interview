"""
problem 01.06 Compress String

Description:
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Example 2:
Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
"""

#use two pointers O(n)
class Solution:
    def compressString(self, S: str) -> str:
        start, end = 0, 1
        result = ""
        if not S: return ""
        while end < len(S):
            if S[start] == S[end]:
                end += 1
            else:
                result += S[start] + str(end - start)
                start = end
                end = start + 1
#remember to add another time after loop
        result += S[start] + str(end - start)
        if len(result) < len(S):
            return result
        else:
            return S

            
