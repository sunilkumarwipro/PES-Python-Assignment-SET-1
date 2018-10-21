i=1 
reverse=False
while i>=1 and i<=10:
    if i==10:
        reverse=True
        print(i)
    if reverse is False:
        print(i)
        i+=1
    elif reverse is True:
        print(i)
        i-=1
mystring="Hello world"
for i in mystring:
    print(i)