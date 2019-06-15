s1,s2=map(str,input().split())
le=len(s1)
d={}
c=0
for i in range(le):
    if(s1[i] not in d.keys()):
        d[s1[i]]=s2[i]
    else:
        if(d[s1[i]]==s2[i]):
            continue
        else:
            c=1
            break
if(c==1):
    print("no")
else:
    print("yes")
