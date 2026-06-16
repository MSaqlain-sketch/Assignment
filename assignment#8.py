# 2. Generate the sum of the series using loops.
starting=int(input("Enter a starting number :"))
ending=int(input("Enter a ending number :"))
print("Sum Of Even Number")
sum=0
for i in range(starting,ending+1):
    if i%2==0:    
        sum=sum+i        
        print(i)
print("The Sum Of The Series Is",sum)