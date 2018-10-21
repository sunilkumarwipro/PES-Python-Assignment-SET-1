names=['sunil','sai','mukunda','hymavathi','venamma']
print("using membership operator")
for i in names:
    if i in names:
        print(i," is present in the list")
print("\nwithout membership operator")
for i in names:
    for j in names:
        if j==i:
            print(j," is present in the list")
names.reverse()
print(names)
    