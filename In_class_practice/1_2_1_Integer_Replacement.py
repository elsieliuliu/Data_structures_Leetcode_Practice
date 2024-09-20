'''
Problem #1: Integer Replacement
Problem on Leetcode: 397_Integer Replacement


Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
Tip: Java programmers should treat Integer.MAX_VALUE() as a special case.


Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2
'''
class Solution:
    def __init__(self):
        self.cache = {1: 0}
    def integerReplacement(self, n: int) -> int:
        if n not in self.cache:
            if n % 2 == 0:
                self.cache[n] = 1 + self.integerReplacement(n//2)
            else:
                self.cache[n] = 1 + min(self.integerReplacement(n-1), self.integerReplacement(n+1))
        return self.cache[n]

#test
n = 8
solution = Solution()
print(solution.integerReplacement(n))

