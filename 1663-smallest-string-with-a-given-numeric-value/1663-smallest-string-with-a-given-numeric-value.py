class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num_a_letra = {
            1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
            8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
            15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
            22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
        }

        if not n or not k:
            return ''

        if(k<n):
            return ''

        aux = []

        for _ in range (n):
            aux.append('a')
        
        k -= n
        i = n - 1
        while (k>0):
            if(k > 25):
                aux[i] = 'z'
                k -= 25
                i -=1
            else:
                aux[i] = num_a_letra[1 + k]
                k = 0
                i-=1
        
        return "".join(aux)