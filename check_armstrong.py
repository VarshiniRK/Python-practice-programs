n=947
def countdigits(n):
    count=0
    while n:
        count=count+1
        n//=10
    return count
def check_armstrong(n):
    #count the digits
    count=countdigits(n)
    print(count)
    sum=0
    tempn=n
    while tempn:
        sum=sum+(tempn%10)**count
        tempn//=10
    if sum==int(n):
        return True
    return False
print(check_armstrong(n))