nu=int(input())
rev=0
while(nu!=0):
    d=nu%10
    rev=rev*10 +d
    nu//=10
print(rev)
