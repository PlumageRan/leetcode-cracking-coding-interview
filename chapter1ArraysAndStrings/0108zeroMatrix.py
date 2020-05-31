"""
problem 01.08 Zero Matrix

Description:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zero-matrix-lcci
"""

#use two sets to record 0 elements' two indexes O(m*n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        row = set()
        col = set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(w):
                matrix[i][j] = 0
        for j in col:
            for i in range(h):
                matrix[i][j] = 0
