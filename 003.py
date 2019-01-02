"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        tmp = []
        for i in s:
            if i in tmp:
                if len(result) < len(tmp):
                    result = tmp
                tmp = tmp[tmp.index(i)+1:] + [i]
            else:
                tmp.append(i)
        if len(result) < len(tmp):
            result = tmp
        return len(result)
