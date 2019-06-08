ro=input()
d={'I':1,'IV':4,'V':5,'IX':9,'X':10}    
def ten(n):
    nu=0
    if(n in d):
        nu=d[n]
    else:
        l=list(n)
        for x in l:
            nu+=d[x]
    return nu
if(ro[0]=='X'and len(ro)!=1 ):
    res=10
    for i in range(1,len(ro)):
        res+=ten(ro[i])
else:
    res=ten(ro)
print(res)
