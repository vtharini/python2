l,r=map(int,input().split())
l1=[]
c=0
for i in range(1,r+1):
    sq=i*i
    if(sq<=r):
        l1.append(i*i)
    else:
        break
for j in range(l,r+1):
    if(j in l1):
        c+=1
print(c)    
