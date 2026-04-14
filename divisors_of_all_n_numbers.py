n=7

#using loop
for i in range(1,n+1):
    divlist=[]
    for j in range(1,(i//2)+1):
        if i%j==0:
            divlist.append(j)
    divlist.append(i)
    print(divlist)

#using Sieve of Eratosthenes
divisorslist=[[] for i in range(n)]
print(divisorslist)
for i in range(1,n+1):
    #print("i...",i)
    for j in range(i,n+1,i):
        #print("j...",j)
        divisorslist[j-1].append(i)
        #print(divisorslist)
print(divisorslist)
