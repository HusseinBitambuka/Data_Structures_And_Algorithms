class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        q=len(s)//2
        s1=self.longestPalindrome(s[0:q])
        s2=self.longestPalindrome(s[q:])
        answer=""
        n=len(s2)-1
        for i in s1:
            if s1[0]==s2[n]:
            