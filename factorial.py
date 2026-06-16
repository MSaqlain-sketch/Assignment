#num=int(input("Enter a number for fabonaci you want"))
# x=0
# y=1
# for i in range(num):
#     print(x)
#     x,y=y,x+y
# num=int(input("Enter a number for foactorial you want"))
# fact=1
# for i in range(num,0,-1):
#     fact=fact*i
# print(fact)
 #num=int(input("Enter a number to chexk the number is prime or not"))
# count=0

# for i in range(1,num+1):
#     if(num%i==0):
#            count=count+1
# if(count==2):
#     print("number is prime")
# else:
#     print("number is not prime")        
i = 1
while(i >= 1):
    j = 8
    while(j >= i):
        print('*', end=' ')
        j = j - 1       # important: j increment
    print()             # new line after each row
    i = i - 1
for i in range(1,5):
    if i==4:
     for y in range(3,9):
      print(y)
