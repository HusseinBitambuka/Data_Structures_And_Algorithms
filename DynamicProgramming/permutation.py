class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsSorted=sorted(nums)
        table=[]
        table.append(numsSorted)
        for k in numsSorted:
            for l in numsSorted:
                

        