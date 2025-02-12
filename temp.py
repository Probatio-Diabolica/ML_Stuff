f = open("dat.csv","r")
a=f.read()
b:str=""
x=0
while(x<len(a)):
    if a[x]=='#' : b+=","
    else : b+=a[x]
    x+=1
f=open("dat.csv","w")
f.write(b)

