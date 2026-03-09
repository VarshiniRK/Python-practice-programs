import math
n=2342345
#Last digit - check the remainder by dividing by 10
lastdigit=n%10
print(lastdigit)

#first digit
#by looping - divide continously by 10 and take the quotient
while n>10:
    n=int(n)/10
print(int(n))
#without looping using the log n to find the number of times to divide by 10(ie lenth -1 will be identified using log)
n=2342345
digits=int(math.log10(n))
firstdigit = int(n/pow(10,digits))
print(firstdigit)

#using string operations to find the first and last digit
n=str(n)
print(n[-1])
print(n[0])

