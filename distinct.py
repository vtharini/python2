w=int(input())
l=list(map(int,input().split()))
def count(e):
    c=0
    for i in l:
        if(i==e):
            c+=1
    return c
for i in l:
    c=count(i)
    if(c==1):
        print(i)
