st=input()
l=list(st)
f=0
for x in l:
    c=ord(x)
    if(c<48 or c>57):
        f=1
        break
if(f==0):
    print("yes")
else:
    print("no")
