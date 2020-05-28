"""
problem 01.07 Rotate Matrix

Description:
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Example 1:
Given matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
"""
#in place O(n^2)
#j 	 , N-1-i = i    , j
#N-1-i, N-1-j = j    , N-1-i
#N-1-j, i     = N-1-i, N-1-j
#i    , j     = N-1-j, i
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i],matrix[i][j] = matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]

#flip than zip O(n)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])