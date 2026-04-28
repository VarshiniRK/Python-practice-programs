n=36
x=int(n**0.5)
print(x)
sum=0
for i in range(1,x+1):
    if n%i==0:
        sum+=i
        print("Divisors :",i)
        if n/i!=n and i!=n/i:
            print("Divisors :",n/i)
            sum+=int(n/i)
print(sum)
if sum==n:
    print("True")
else:
    print("False")