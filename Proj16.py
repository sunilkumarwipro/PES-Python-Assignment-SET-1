def checkprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
n=int(input("Enter a number"))
if checkprime(n) is True:
    print(n," is a prime number")
else:
    print(n," is not a prime number")
for i in range(1,n+1):
    if checkprime(i) is True:
        print(i)