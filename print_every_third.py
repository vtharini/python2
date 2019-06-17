st=input()
l=list(st)
st1=''
for i in range(len(l)):
    if(i%3==0):
        st1+=l[i]
print(st1)
