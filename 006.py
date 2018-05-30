"""
Name: ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        zigzag = ""
        if numRows == 1:
            return s
        while i < numRows:
            
            if i == 0 or i == (numRows - 1):
                j = i
                while j < len(s): 
                    zigzag += s[j]
                    j += 2*numRows - 2
                    
            else:
                j = i
                count = 0
                while j < len(s): 
                    zigzag += s[j]
                    if count %2 == 0:
                        j += 2*numRows - 2*i - 2
                        count +=1
                    else:
                        j += 2*i
                        count +=1
                    
            i +=1
        return zigzag
