class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        if not boxTypes or not truckSize:
            return 0
        
        boxTypes.sort(key=lambda x: x[1], reverse=True) 
        
        toReturn = 0
        cajas = 0
        for pos in boxTypes:
            if(cajas + pos[0]<= truckSize):
                toReturn += pos[0] * pos[1]
                cajas += pos[0]
            elif(cajas + pos[0] > truckSize and cajas < truckSize):
                cajasFaltantes = truckSize - cajas
                toReturn += cajasFaltantes * pos[1]
                cajas = truckSize

        return toReturn