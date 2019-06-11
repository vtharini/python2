st=input()
l=list(st)
d={}
max=0
r=0
for i in range(len(l)):
    if(l[i]!=' '):
        d[l[i]]=l.count(l[i])
for k,v in d.items():
    if(v>max):
        max=v
        r=k
print(str(r))
