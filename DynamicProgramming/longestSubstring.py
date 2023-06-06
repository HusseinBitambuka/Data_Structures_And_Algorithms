def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        hash={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        solution=0
        stack=[]
        for i in range (len(s)):
            solution=solution+hash[s[i]]
            if len(stack)>0:
                checker=stack.pop()
                if checker=="I" and s[i]=="V" or s[i]=="X":
                    solution=solution-1
                elif checker=="X" and s[i]=="L" or s[i]=="C":
                    solution=solution-10
                elif checker=="C" and s[i]=="D" or s[i]=="M":
                    solution=solution-100
                stack.append(s[i])
            stack.append(s[i])
        return solution


s="DXCI"
print(romanToInt(s))