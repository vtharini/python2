st=input()
l=list(st)
st1=''
for x in l:
    if(x.islower()==True):
        st1+=x.upper()
    else:
        st1+=x.lower()
print(st1)
        
