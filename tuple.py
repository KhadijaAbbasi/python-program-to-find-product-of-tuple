#tuple=(1,'k',33.33,(2,),['blue','green'])
t1=(4,3,2,2,-1,18)
t2=(2,4,8,8,3,2,9)
product=1
for x in range(len(t1)):
    product=product*t1[x]
print("Product of 1st tuple is :",product)
pro=1
for x in range(len(t2)):
    pro=pro*t2[x]
print("Product of 2nd tuple is :",pro)