nu=int(input())
l=[]
pf=[]
for i in range(2,nu+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        l.append(i)
for x in l:
    if(nu%x==0):
        pf.append(x)
print(*pf)
