string1=input("Enter a string")
for i in string1:
    print(i)
for i in range(0,len(string1)+1):
    print(string1[i:])
print(string1*100)
string2=input("Enter another string")
print(string1+string2)