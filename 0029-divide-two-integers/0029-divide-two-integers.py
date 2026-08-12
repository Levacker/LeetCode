class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Limite entero de 32 bits
        MAX_INT = 2147483647      # 2^31 - 1
        MIN_INT = -2147483648     # -2^31

        # Caso especial de overflow/desbordamiento
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determinar si el resultado es negativo
        negativo = (dividend < 0) ^ (divisor < 0)

        # Trabajar con valores absolutos
        a, b = abs(dividend), abs(divisor)
        resultado = 0

        # Algoritmo de restas por potencias de 2 (desplazamiento de bits)
        while a >= b:
            temp = b
            m = 1
            # Duplicamos temp (b * 2^k) mientras quepa en 'a'
            while a >= (temp << 1):
                temp <<= 1
                m <<= 1
            
            a -= temp
            resultado += m

        if negativo:
            resultado = -resultado

        # Asegurar que el resultado no se salga del rango de 32 bits
        return max(MIN_INT, min(MAX_INT, resultado))
        return toReturn