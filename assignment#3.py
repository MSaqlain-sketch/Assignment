# 3. Find the maximum and minimum values from inputted numbers.
a=int(input("Enter First Number :")) 
b=int(input("Enter Second Number :")) 

if (a>b):
    print("Maximum =",a)
    print("Minimum =",b)
elif (b>a):
       print("Maximum =",b)
       print("Minimum =",a) 
else:
    print("Both are equal")