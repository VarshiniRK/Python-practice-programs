import math
n=-3534252
count=0
#Approach 1 : without length function | by using mathematical operations - do floor division to remove the right most digit 
# and increment the count by 1, do this till the n becomes zero
if n==0:
    count =1
while n>0:
    n= n //10
    print(n)
    count +=1
print("Count : ",count) 

#Approach 2 : Do the same floor division but by using recursive function
def countdigits(n):
    #floor division of negative number will never becomes 0 so convert it into a postive number first
    n=abs(n)
    if n//10==0:
        return 1
    return 1 + countdigits(n//10)
n=3534252
print("count :",countdigits(n))

#Approach 3 : Using math.log10
print("count : ", int(math.log10(n))+1)

#Approach 4 : Using length function
print("count : ", len(str(n)))
