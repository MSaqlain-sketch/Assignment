# # 1. Generate a number series (even, odd, prime, Fibonacci, etc.) by taking the
# # starting and ending point input.
# starting=int(input("Enter a starting number :"))
# ending=int(input("Enter a ending number :"))
# print("Even Number Series")
# for i in range(starting , ending+1):
#     if i % 2 == 0:
#         print(i)
# # 1. Generate a number series (even, odd, prime, Fibonacci, etc.) by taking the
# # starting and ending point input.
# start=int(input("Enter a starting number :"))
# end=int(input("Enter a ending number :"))
# print("Odd Number Series")
# for i in range(start,end+1):
#     if i % 2 !=0:
#         print(i)
# # 1. Generate a number series (even, odd, prime, Fibonacci, etc.) by taking the
# # starting and ending point input.
# start=int(input("Enter a starting point :"))
# end=int(input("Enter a ending point :"))
# print("Prime Number Series")
# for num in range(start ,end + 1):
#     if num > 1:
#         prime = True
#         for i in range(2,num):
#             if num % i == 0:
#                 prime = False
#                 break
#         if prime:
#          print(num)

# # 1. Generate a number series ( Fibonacci,) by taking the
# # starting and ending point input.
start=int(input("Enter a starting number :"))
end=int(input("Enter a ending number :"))
print("Fibonacci Series")
a=0 
b=1
for i in range(1,end+1):
    if i>=start:
     print(a)
     c=a+b
     a=b
     b=c