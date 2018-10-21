n=-10
a,b,fib=0,1,0
if n==1:
    print(a)
elif  n>1:
    count=1
    while count<=n:
        print(a)
        fib=a+b
        a=b
        b=fib
        count+=1