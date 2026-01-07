n = 4
arr = [57,57,-57,57]
firstmax=arr[0]
#should not be assigned to zero to handle negative values
secondmax=None
for i in arr[1:]:
    if i>firstmax:
        secondmax=firstmax
        firstmax=i
    elif secondmax is not None and i<firstmax and i>secondmax:
        secondmax=i
    elif secondmax is None and i<firstmax:
        secondmax=i 
    print("Firstmax :",firstmax)
    print("Secondmax",secondmax)
print(secondmax)
