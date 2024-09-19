'''
Problem 1: Substring

Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.

NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).


Example 1:
Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false



#########sliding window########################


pseudocode:

1. edge cases:
if large_str < potential_str: return False
if any of them is empty: return False

2. loop through the large_str, try to find the matching letter.
******trick: use an int var to indicate the current matching lengths and the index(pointer) of potential
substr, this var starts with 0, only update it when matching******
count_size = 0
for i in range(len(large_str)):
    if large_str[i] == potential[count_size]:
      count_size += 1
      if count_size == len(potential_str):
        return True
    else:
      count_size = 0
return False

'''
class Solution:
    def Substring(self, large_str, potential_substr):
        if len(large_str) < len(potential_substr):
            return False
        if not large_str or not potential_substr:
            return False

        count = 0
        for i in range(len(large_str)):
            if large_str[i] == potential_substr[count]:
                count += 1
                if count == len(potential_substr):
                    return True
            else:
                count = 0

        return False



large_str = "dcat"
potential_substr = "cat"
solution = Solution()
print(solution.Substring(large_str,potential_substr))

'''
Time Complexity: O(n)

'''