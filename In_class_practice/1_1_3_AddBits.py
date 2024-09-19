'''
Problem 3: Add Binary
Problem on Leetcode: 67


Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

#############################
解法一： 我自己的思路，padding 0s
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        diff = max(len(a), len(b)) - min(len(a), len(b))
        if len(a) < len(b):
            a = ('0' * diff) + a
        if len(b) < len(a):
            b = ('0' * diff) + b
        i = max(len(a), len(b)) - 1
        res = []
        carry = 0
        while i >= 0:
            sum = int(a[i]) + int(b[i]) + carry
            if sum == 0:
                res.append('0')
                carry = 0
            elif sum == 1:
                res.append('1')
                carry = 0
            elif sum == 2:
                res.append('0')
                carry = 1
            else:
                res.append('1')
                carry = 1
            i -= 1

        if carry == 1:
            res.append('1')
        return ''.join(res)[::-1]









a = "1010"
b = "1011"
solution = Solution()
print(solution.addBinary(a, b)) #expexted "10101"

a = "1"
b = "11"
solution = Solution()
print(solution.addBinary(a, b)) #expexted "10101"

