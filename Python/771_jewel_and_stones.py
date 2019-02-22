class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jewels = 0
        for j in J:
            for s in S:
                if j == s:
                    jewels += 1
        return jewels
