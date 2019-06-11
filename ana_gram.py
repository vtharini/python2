l=['k','a','b','a','l','i']
def check(st):
    lis=list(st)
    for i in lis:
        if(i in l):
            if(l.count(i)<=lis.count(i)):
                continue
            else:
                return 0
                break
        else:
            return 0
            break
    else:
        return 1
n=int(input())
l1=[]
c=0
for i in range(n):
    s=input()
    l1.append(s)
for i in l1:
    r=check(i)
    if(r==1):
        c+=1
print(c)
    
        
