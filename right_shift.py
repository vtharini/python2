w,s=map(int,input().split())
li=list(map(int,input().split()))
for x in range(s):
    for i in range(w-1,0,-1):
        li[i],li[i-1]=li[i-1],li[i]
print(*li)
