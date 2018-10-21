A=[101,102,103,104,105,106,107,108,109,110]
B=['sunil','sai','mukunda','hymavathi','malik','imran','siva','vikram','venamma','dinesh']
print(B)
for i in A:
    print(B[A.index(i)])
print(B[4:10])
print(B[3:])
n=int(input("Enter a value"))
for i in range(1,len(B)):
    print(B[i]*n)
print(A+B)
for i in range(0,len(A)):
    print(A[i]," ",B[i])