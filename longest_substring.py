# o(n)
s="abcdefghijklmnopqrstuvwxyz" * 10000
lastseen={}
left=0
best=0
for right, char in enumerate(s):
    if char in lastseen and lastseen[char]>=left:
        left=lastseen[char]+1
    lastseen[char]=right
    best=max(best,right-left+1)

print(best)

#o(n^2)

s="abcdefghijklmnopqrstuvwxyz" * 10000
finalsubstring=""
substring=""
n=0
if len(s)==1:
    print(len(s))
else:
    while n<len(s)-1:
        substring=""
        #print("working on batch : ",s[n:])
        for i in s[n:]:
            if i in substring:
                break
            else:
                substring=substring+i
        #print("substring",substring)
        if len(substring)>len(finalsubstring):
            finalsubstring=substring
        n=n+1
    #print(finalsubstring)
    print(len(finalsubstring))