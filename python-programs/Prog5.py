from sys import argv
for i in argv[1:6]:
    print(i)
if eval(argv[1])>eval(argv[2]) and eval(argv[1])>eval(argv[3]):
    print(argv[1]," is the biggest number")
elif eval(argv[2])>eval(argv[1]) and eval(argv[2])>eval(argv[3]):
    print(argv[2]," is the biggest number")
else:
    print(argv[3]," is the biggest number")