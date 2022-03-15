a=input("enter any string :")
l=list(a.split())
c=0
for i in l:
    b=[c][ ::-1]
    if l[c]==b:
        c=c+1
        print(l[c])
        print("total{} palidrome word instring{}".format(c,l[c]))
   
