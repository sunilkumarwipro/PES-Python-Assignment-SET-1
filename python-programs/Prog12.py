a=[]
total,avg=0,0
for i in range(1,11):
    a.insert(i-1,int(input("Enter a number\n")))
    total+=a[i-1]
avg=total/len(a)
print("Numbers less than average")
for i in a:
    if i<avg:
        print(i)
print("Numbers grearer than average")
for i in a:
    if i>avg:
        print(i)
print("Numbers equal to average")
for i in a:
    if i==avg:
        print(i)