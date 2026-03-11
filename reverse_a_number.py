#Through looping
n=34239
reversed_number=0
while n>0:
    digit=n%10
    reversed_number=reversed_number*10+digit
    n=n//10
print(reversed_number)
#Time Complexity - O(log n)
#Space Complexity - O(1)

#Through recursion
n=34239
def reverse_number(n,rev=0):
    if n==0:
        return rev
    return reverse_number(n//10,rev * 10+(n%10))
print(reverse_number(n))
#Time Complexity - O(log n)
#Space Complexity - O(log n)

#Using reverse function of list
n=34239
n=str(n)
n=list(n)
n.reverse()
reversed_num=int("".join(n))
print(reversed_num)
#Time Complexity - O(log n)
#Space Complexity - O(1)


#using slicing
n=34239
n=str(n)
reverse_number=n[ : :-1]
print(reversed_number)
#Time Complexity - O(n)
#Space Complexity - O(n)