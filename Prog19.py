for i in range(1,100+1):
    if i%2==0:
        if i==50:
            break
        if i in [10,20,30,40,50]:
            continue
        print(i)
i=51
while i<=100:
    if i==90:
        i+=1
        break
    if i in [60,70,80,90]:
        i+=1
        continue
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
        