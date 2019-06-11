l,u=list(map(int,input().split()))
i=l
res=0
while(res==0):
    if(i%l==0 and i%u==0):
        res=i
    else:
        i+=1
print(res)
