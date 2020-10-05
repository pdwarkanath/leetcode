"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int):
        sums = {0:1}
        result = 0
        cum_sum = 0
        for i in nums:
            cum_sum += i
            temp_sum = cum_sum - k
            try:
                sums[cum_sum] += 1
            except KeyError:
                sums[cum_sum] = 1
            try:
                if k == 0:
                    result += sums[temp_sum] - 1
                else:
                    result += sums[temp_sum]
            except KeyError:
                pass
        return result
