w=int(input())
l=list(map(str,input().split()))
l1=sorted(l,key=len)
for i in range(w-1):
    if(len(l1[i])==len(l1[i+1]) and l1[i]>l1[i+1]):
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(*l1)
