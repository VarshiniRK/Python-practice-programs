#Two pointers
#you dont need a new variable, you can replace within the same variable
#Loop until start is less than end
text="coding"
start =0
end=len(text)-1
text=list(text)
while start<end:
    if start==end:
        pass
    text[start],text[end]=text[end],text[start]
    start+=1
    end-=1
print("".join(text))

#Using stack approach and poping it from the stack
text=list("coding")
reversedtext=[" "]*len(text)
for i in range(len(text)):
    reversedtext[i]=text.pop()
print("".join(reversedtext))

#Using Recursion
def reverse_string(text,left,right):
    if left>right:
        return "".join(text)
    text[left],text[right]=text[right],text[left]
    return reverse_string(text,left+1,right-1)
text="coding"
print(reverse_string(list(text),0,len(text)-1))
    
