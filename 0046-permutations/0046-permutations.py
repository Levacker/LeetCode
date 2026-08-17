class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        aux, sol = [], []

        def backtracking():
            if (len(aux) == n):
                sol.append(aux[:])
                return 
            
            for x in nums:
                if x not in aux:
                    aux.append(x)
                    backtracking()
                    aux.pop()
            
        backtracking()
        return sol