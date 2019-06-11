l1=['k','a','b','a','l','i']
def check(st):
    lis=list(st)
    for i in lis:
        if(i in l1):
            if(l1.count(i)<=lis.count(i)):
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
l2=[]
c=0
for i in range(n):
    s=input()
    l2.append(s)
for i in l2:
    r=check(i)
    if(r==1):
        c+=1
print(c)
    
        
