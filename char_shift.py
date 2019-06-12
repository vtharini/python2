st=input()
l=list(st)
new_l=[]
d={'X':'A','Y':'B','Z':'C','x':'a','y':'b','z':'c'}
for x in l:
    if x in d:
        new_l.append(d[x])
    else:
        new_l.append(chr(ord(x)+3))
st="".join(new_l)
print(st)
