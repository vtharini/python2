a,b=map(int,input().split())
m=max(a,b)
l=[]
for i in range(1,m+1):
    if(a%i==0 and b%i==0):
        l.append(i)
print(max(l))
