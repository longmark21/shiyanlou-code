for i in range(1,101):
    if i<10 and i%7!=0:
        print(i)
    elif i>=10 and i%10!=7 and i%7!=0 and i//10!=7:
        print(i)
