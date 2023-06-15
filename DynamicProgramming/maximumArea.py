def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        return max(len(height)*height[len(height)-1],self.maxArea(height[:len(height)-1]))