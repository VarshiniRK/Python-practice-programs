# Prime numbers is divisible exactly by one and itself
import time
def isprime(numb):
    #check if the given number is divisible by i which ranges from 2 till the square root of the given number
    #why square root of the given number => if numb has any divisor other than one and itself it will be less than √n because √n * √n = n 
    factors= lambda numb: [i for i in range(2,int(numb**0.5)+1) if numb%i==0] if numb>2 else []
    #primenumbers= lambda x : [i for i in range(2,numb+1) if len(factors(i))==1]
    return True if len(factors(numb))==0 else False
currentprime=1
while True:
    inp=input("Do you want to see the next prime number enter Yes/No ")
    if inp.lower().startswith("n"):
        break
    elif inp.lower().startswith("y"):
        currentprime+=1
        while not isprime(currentprime):
            currentprime+=1
        print("Next prime number is : ", currentprime)
    else:
        print("Your Input is not valid. Try again.")
    time.sleep(1)

