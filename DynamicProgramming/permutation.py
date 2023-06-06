class Solution(object):
    def maximum(self,s):
        for i in range (len(s)):
            if s[0]=="?":
                if s[1]=="?":
                    s[0]="2"
                elif int(s[1])<3:
                    s[0]="2"
                else:
                    s[0]="1"
            if s[1]=="?":
                if s[0]=="2":
                    s[1]="3"
                else:
                    s[1]="9"
            if s[3]=="?":
                s[3]="5"
            if s[4]=="?":
                s[4]=="9"

inputTest="?4:5?"       
mido=Solution()
print(mido.maximum(inputTest))


        