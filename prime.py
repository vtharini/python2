u,v=input().split()
c=0
for x in range(int(u),int(v)+1):
    for y in range(2,i):
        if(u%v==0):
            break
    else:
        c+=1
print(c)
