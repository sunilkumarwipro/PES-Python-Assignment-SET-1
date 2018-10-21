a=[]
for i in range(1,5):
    a.insert(i,int(input("Enter a number")))
print("Biggest number among 4 numbers")
if a[0] > a[1] and a[0] > a[2]:
    if a[0] > a[3]:
        print(a[0],"is the biggest number")
    else:
        print(a[3],"is the biggest number")
elif a[1] > a[2] and a[1] > a[3]:
        print(a[1],"is the biggest number")
elif a[2] > a[3]:
    print(a[2],"is the biggest number")
else:
    print(a[3],"is the biggest number")


a.append(int(input("Enter a number"))) 
print("Biggest number among 5 numbers")

if a[0] > a[1] and a[0] > a[2] and a[0] > a[3]:
     if a[0] > a[4]:
        print(a[0],"is the biggest number")
     else:
       print(a[4],"is the biggest number")
elif a[1] > a[2] and a[1] > a[3] and a[1] > a[4]:
    print(a[1],"is the biggest number")
elif a[2] > a[3] and a[2] > a[4]:
      print(a[2],"is the biggest number")
elif a[3] > a[4]:
     print(a[3],"is the biggest number")
else:
    print(a[4],"is the biggest number")