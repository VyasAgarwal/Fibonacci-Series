x=int(input("Number of Terms :"))
a=0
b=1
count = 0
if x <= 0: 
    print("Please enter a positive number")
elif x == 1:
    print("Series upto", x , ":")
    print(a)
else:
    print("Fibonacci Series:")
    while count < x:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
