# # # # 2 4 6 8 10
# # # # 2 4 6 8
# # # # 2 4 6
# # # # 2 4
# # # # 2
# # # # for i in range(2,11,+2):
# # # #     for j in range(2,14-i,2):
# # # #        print(j ,end =" ")  
# # # #     print( ) 

# # # # # 0 1 1 2 3 5 8 ...
# # # # a=0
# # # # b=1

# # # # for num in range(0,8):
# # # #  print(a,end ="  ") 
# # # #  c=a+b
# # # #  a=b
# # # #  b=c
# # # # 1 3 5 7 9
# # # # 1 3 5 7
# # # # 1 3 5
# # # # 1 3
# # # # 1
# # # # for num in range(1,10,2):
# # # #     for j in range(1,12-num,1):
# # # #      if j%2!=0:
# # # #       print(j,end = " ")
# # # #     print()

# # # # # 10 8 6 4 2
# # # # # 8 6 4 2
# # # # # 6 4 2
# # # # # 4 2
# # # # # 2
# # # # for num in range(10,1,-2):
# # # #    for j in range(num,0,-2):
# # # #     print(j,end=" ")
# # # #    print()  

# # # # # 2 4 6 8 10
# # # # # 4 6 8 10
# # # # # 6 8 10
# # # # # 8 10
# # # # # 10
# # # # for j in range(2,11,2):
# # # #    for i in range(j,12,2):
# # # #      print(i,end=" ")
# # # #    print()

# # # # # 1 2 3 4 5
# # # # # 2 3 4 5
# # # # # 3 4 5
# # # # # 4 5
# # # # # 5
# # # # for num in range(1,6):
# # # #    for j in range(num,6,1):
# # # #     print(j,end=" ")
# # # #    print()   

# # # # # 1
# # # # # 1 3
# # # # # 1 3 5
# # # # # 1 3 5 7
# # # # # 1 3 5 7 9
# # # # for num in range(1,10,2):
# # # #   for i in range(1,num+1,2):
# # # #     print(i,end=" ")
# # # #   print()

# # # # 5
# # # # 5 4
# # # # 5 4 3
# # # # 5 4 3 2
# # # # 5 4 3 2 1
# # # for i in range(5,0,-1):
# # #    for j in range(5,i-1,-1):
# # #     print(j,end=" ")
# # #    print() 

# # # 10 8 6 4 2
# # # 8 6 4 2
# # # 6 4 2
# # # 4 2
# # # 2
# # for num in range(10,1,-2):
# #     for j in range(num,0,-2):
# #      print(j,end=" ")
# #     print()  

# # # 1 2 3 4 5
# # # 2 3 4 5 6
# # # 3 4 5 6 7
# # # 4 5 6 7 8
# # # 5 6 7 8 9

# # for i in range(1,6):
# #    for j in range(i,i+5):
# #     print(j,end=" ")
# #    print()       

# # 1 2 3 4 5
# # 3 4 5 6 7
# # 5 6 7 8 9
# # 7 8 9 10 11
# # 9 10 11 12 13
# # for num in range(1,10,2):
# #    for j in range(num,num+5):
# #     print(j,end=" ")
# #    print()


# # 1
# # 2 1
# # 3 2 1
# # 4 3 2 1
# # 5 4 3 2 1
# for num in range(0,5):
#    for j in range(num+1,0,-1):
#     print(j,end=" ")
#    print()

# # 1 1 1 1 1
# # 2 2 2 2 2
# # 3 3 3 3 3
# # 4 4 4 4 4
# # 5 5 5 5 5
# for num in range(1,6):
#    for j in range(1,6):
#       print(num,end=" ")
#    print()  

# 2 4 6 8
# 4 6 8 10
# 6 8 10 12
# 8 10 12 14
# for i in range(2,10,2):
#    for j in range(i,i+8,2):
#     print(j,end=" ")
#    print() 
# 4321
# 432
# 43
# 1
# for i in range(4,0,-1):
#    if i==1:
#       print(i)
#    else:   
#      for j in range(4,1,-1):
#       print(j,end=" ")
#      print() 

# Write a program to develop a basic billing system for a grocery store that
# i. takes the price and quantity of two different items from the user.
# ii. calculates the total cost for each item and the grand total.
# iii. applies a 10% discount if the grand total is more than Rs 1000.
# iv. displays all calculated values.
# v. compares and displays the item that is more expensive based on the total
#  cost.

price=int(input("Enter the price"))
quantity_1=int(input("Enter the quantity of item"))
quantity_2=int(input("Enter the quantity of item"))
t_cost=100*(quantity_1)
t_cost=100*(quantity_2)
g_total=t_cost+t_cost
if g_total>1000:
   price=price*10/100
print(price)