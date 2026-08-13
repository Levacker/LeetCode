class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        aux = nums1 + nums2

        aux.sort()

        if(len(aux) % 2 == 0):
            medio = len(aux) // 2
            medio2 = medio - 1
            return (aux[medio] + aux[medio2]) / 2.0
        else:
            medio = len(aux) // 2
            return aux[medio]