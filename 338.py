"""
Name: Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""

class Solution(object):
    import math
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        result = [0,1]
        x = 1
        for i in range(2,num+1):
            log2 = int(math.log(i,2))
            x += 1
            for j in range(1,log2+1):
                if i % 2**j == 0:
                    x -= 1
                else:
                    break
                
            result.append(x)
        return result