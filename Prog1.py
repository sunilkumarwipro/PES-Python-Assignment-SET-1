from operator import add,sub,mul,truediv 
a=int(input("Enter a number"))
b=int(input("Enter another number"))
for op in [add,sub,mul,truediv] :
      print(op(a,b))