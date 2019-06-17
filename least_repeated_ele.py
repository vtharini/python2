st=input()
l=list(st)
l1=[]
c=len(l)
for i in range(len(l)):
        if(l[i]!=' ' and l[i] not in l1 and l.count(l[i])==1):
            a=l[i].lower()
            l1.append(a)
print(*l1)
