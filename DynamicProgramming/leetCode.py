from collections import deque
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer=ListNode() # the return linked-list
        checker=True
        addOne=False
        stack=[]
        while checker:
            if not addOne:
                sumNumber=l1.val+l2.val
                if sumNumber>=10:
                    addOne=True
                    stringSum=str(sumNumber)
                    numToAdd=int(stringSum[-1])
                    stack.append(numToAdd)
                else:
                    addOne=False
                    stack.append(sumNumber)
                    
            else:
                sumNumber=l1.val+l2.val+1
                addOne=False
                if sumNumber>=10:
                    addOne=True
                    stringSum=str(sumNumber)
                    numToAdd=int(stringSum[-1])
                    stack.append(numToAdd)
                else:
                    addOne=False
                    stack.append(sumNumber)
            if not l1.next:
                checker=False
            l1=l1.next
            l2=l2.next
        answer.val=stack.pop()
        for i in range(len(stack)):
            newNode=ListNode(stack.pop())
            newNode.next=answer
            answer=newNode
        return answer
    
li1=ListNode(2)
li1.next=ListNode(4)
li1.next.next=ListNode(3)
li1.next.next.next=ListNode(4)


li2=ListNode(5)
li2.next=ListNode(6)
li2.next.next=ListNode(4)
li2.next.next.next=ListNode(5)
mido=Solution()
solution=mido.addTwoNumbers(li1,li2)

cheker=True
while cheker:
    print(solution.val)
    if not solution.next:
        cheker=False
    solution=solution.next

h=str(12156)
print(int(h))




