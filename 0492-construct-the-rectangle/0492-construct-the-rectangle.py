class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if not area:
            return [0,0]

        largo = area
        ancho = 1
        divisor = 1
        
        while(divisor * divisor <=area):
            if(area % divisor == 0):
                largo = area // divisor
                ancho = divisor
            divisor +=1

        return [largo, ancho]