# Runtime: 52 ms, faster than 89.46% of Python solutions.
# Memory Usage: 11.7 MB, less than 11.06% of Python solutions.

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rev = 0 # reverse flag
        l = ["" for i in range(numRows)]
        row = 0
        for let in s:
            if rev == 0:
                l[row] += let
                if row < numRows - 1:
                    row += 1
                elif row >= numRows - 1:
                    row -= 1
                    rev = 1
            elif rev == 1:
                l[row] += let
                if numRows - 1 >= row > 0:
                    row -= 1
                elif row == 0:
                    row += 1
                    rev = 0
        output = ""
        for str in l:
            output += str
        return output
