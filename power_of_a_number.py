n=2
x=4
# reversed_digit=0
# while x>0:
#     digit=x%10
#     reversed_digit= reversed_digit*10+digit
#     x=x//10
# print(reversed_digit)
# x=reversed_digit

#By Looping
#Instead of multiplying every digit, multiply only till half of it
n=2
x=100
powered_number=1
for i in range(x//2):
    powered_number*=n
if x%2==0:
    powered_number*=powered_number
else:
    powered_number*=powered_number*n
print(powered_number)

#By Recursion
n=2
x=100
def power_of_a_function(n,x):
    if x==1:
        return n
    powered_number= power_of_a_function(n,x//2)
    if x%2==0:
        powered_number*=powered_number
    else:
        powered_number*=powered_number*n
    return powered_number
print(power_of_a_function(n,x))

#Using ** operator or the pow function
n=2
x=100
print(n**x)
print(pow(n,x))






