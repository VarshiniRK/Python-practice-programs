n=64
#1x20
#10x2
sqrtvalue=int(n**0.5)
divisors=[1,n]
for i in range(2,sqrtvalue+1):
    if n%i==0:
        divisors.append(i)
        if sqrtvalue !=i:
            divisors.append(n//i)

print(divisors)

def divisor_of_a_number(n,i):
    #print(n,"....",i,".....")
    if i==1:
        if n==1:
            return [1]
        else:
            return [1,n]
    else:
        if n%i==0:
            if i!=n//i:
                div=n//i
                return [i]+[div]+divisor_of_a_number(n,i-1)
            return [i]+divisor_of_a_number(n,i-1)
        return divisor_of_a_number(n,i-1)

print(divisor_of_a_number(n,int(n**0.5)))

def divisor_of_a_number(n,i,finalist):
    print(n,"....",i,".....",finalist)
    if i==1:
        if n==1:
            return [1]
        else:
            return finalist + [1,n]
    else:
        if n%i==0:
            if i!=n//i:
                div=n//i
                finalist.extend([i,div])
            else:
                finalist.extend([i])
        return divisor_of_a_number(n,i-1,finalist)
finalist=[]
print(divisor_of_a_number(n,int(n**0.5),finalist))



