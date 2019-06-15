s1,s2=map(str,input().split())
d={}
c=0
for i in range(len(s1)):
    if(s1[i] not in d.keys()):
        d[s1[i]]=s2[i]
    else:
        if(d[s1[i]]==s2[i]):
            continue
        else:
            c+=1
if(c==1):
    print("yes")
else:
    print("no")
