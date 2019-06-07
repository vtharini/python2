s1=input()
l=list(s1)
for i in range(len(l)-1):
    if(i%2==0):
        l[i],l[i+1]=l[i+1],l[i]
s1="".join(l)
print(s1)
