p,p1=map(int,input().split())
p2,p3=map(int,input().split())
p4,p5=map(int,input().split())
if(p==p2 and p2==p4):
    print("yes")
elif(p1==p3 and p3==p5):
    print("yes")
elif(p==p1 and p2==p3 and p4==p5):
    print("yes")
else:
    print("no")
