class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """


        longitud = len(colors)
        paraDevolver = 0

        for i in range (longitud):
            if (i==0 and i<longitud-1):
                if(colors[longitud-1] != colors[0] and colors[1] != colors[0]):
                    paraDevolver +=1
            elif(i<longitud-1):
                if(colors[i] != colors[i+1] and colors[i] != colors[i-1]):
                    paraDevolver +=1
            else:
                if(colors[i] != colors[0] and colors[i] != colors[i-1]):
                     paraDevolver +=1
        
        return paraDevolver