class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, elem in enumerate(s):
            if s.find(elem) == s.rfind(elem):
                return i

        return -1