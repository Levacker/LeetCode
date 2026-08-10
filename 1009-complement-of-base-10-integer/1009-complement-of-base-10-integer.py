class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        binario = str(bin(n)[2:])
        paraDevolver = ''
        for i in binario:
            if i == '0':
                paraDevolver+= '1'
            elif i == '1':
                paraDevolver+= '0'

        aux = '0b' + paraDevolver

        return int(aux, 2)