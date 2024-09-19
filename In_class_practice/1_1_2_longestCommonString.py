'''
Problem 2: Longest Common Prefix
Problem on Leetcode: 14


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

##########################################################################

解法1:
to find common prefix, we have to compare each letter of the first string to all others.
bruteforce就是loop套loop。
**难点** 怎么loop
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:   ##解法1
        res = ""
        for i in range(len(strs[0])): ##for each letter in the first string
            for s in strs[1:]:  ##for each string except for the first string
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]  ## strs[0][i] is the current letter we are checking
        return res


    '''time complexity: O(n*m)
    '''
    '''
    ###############################################################################
    
    解法2 
    可以利用python的sort by letters，只需要对比第一个和最后一个str
    '''

    def longestCommonPrefixx(self, strs: list[str]) -> str:
        result = ""
        sorted_strs = sorted(strs)
        for i in range(len(sorted_strs[0])):
            if i == len(sorted_strs[-1]) or sorted_strs[0][i] != sorted_strs[-1][i]:
                return result
            result += sorted_strs[0][i]
        return result

    '''
    Time complexity: O(nlogn + m)
    '''
    '''
    解法3：和解法2类似的原理，不sort，而是找到alphabetically smallest and largest string
    '''
    def longestCommonPrefixxx(self, strs: list[str]) -> str:
        small = min(strs)
        large = max(strs)
        length = min(len(small), len(large))
        for i in range(length):
            if small[i] != large[i]:
                return small[0:i]
        return small[0:length]

    '''
    time complexity: 
    O(n*m)
    '''




strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
print(solution.longestCommonPrefixx(strs))
print(solution.longestCommonPrefixxx(strs))