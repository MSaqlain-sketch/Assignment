# 6. Input multiple values using a loop and calculate the average, maximum, or
# minimum value using a selection statement.
sum=0
n=5
max=-float('inf')
min=float('inf')
for i in range(n):
 a=int(input("Enter a Number"))
 sum=sum+a
 if a<min:
     min=a
 if a>max:
     max=a 
print("mininum number is",min)           
print("maximun number is ",max)
print("Sum",sum)   
print("average=",sum/n)            