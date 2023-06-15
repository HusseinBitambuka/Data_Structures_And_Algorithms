import sys
def solution(s):
    rows={"A":9,"B":9,"C":9,"D":9,"E":9} # let first assume that each row has all its nine seats.
    largest=0 # this answer
    for i in range (len(s)-1): # check all the reserved seats and 
        if s[i].isalpha():
            remain=abs(9-int(s[i+1]))
            rows[s[i]]=abs(rows[s[i]]-remain)
        
    for k in rows:
        largest=max(largest,rows[k])
    return largest


test="B3A4C7E6"
test2="A7B5C5D5E5A9A1"

print(solution(test2))
def solution1(s):
    digits={} # hashtable to check if the letter has a digit already
    k=9 # this is going to be the value of the first letter. I chose nine because it is going to give me the highest value possible
    answer=""# this is the final string that going to collect the answer
    for i in s: 
        if i in digits: # check if the letter has a digit already 
            answer+=str(digits[i]) # if it does, add it to the string
        else: # else
            digits[i]=k #add that letter and its digit to the hashmap
            k-=1 # the second letter should take the second biggest digit available
            answer+=str(digits[i]) # append the digit to the string
    return answer 

test4="BABBC"

print(solution1(test4))
