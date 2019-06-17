nu=int(input())
cnt=0
l=[[0,0,0,0]]
for i in range(nu):
    l1=[0]
    l2=list(map(int,input().split()))
    for i in range(nu):
        l1.append(l2[i])
    l1.append(0)
    l.append(l1)
l.append([0,0,0,0])
for i in range(1,nu+1):
    for j in range(1,nu+1):
        if(l[i][j-1]==l[i][j+1]==l[i-1][j]==l[i-1][j]==0):
            c+=1
print(cnt)
