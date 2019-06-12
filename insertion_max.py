n,k=map(int,input().split())
d=input()
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    l1.append(i)
    print(max(l1),end=" ")
