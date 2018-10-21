def display(v):
    print(v," is the biggest number")
a=int(input("Enter 'A' value"))
b=int(input("Enter 'B' value"))
c=int(input("Enter 'C' value"))
if a>b and a>c:
    display(a)
elif b>c and b>a:
    display(b)
else:
    display(c)f