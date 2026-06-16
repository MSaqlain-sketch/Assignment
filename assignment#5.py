#5. Generate the utility bill based on charges allocated to each unit range. The bill
#should contain the meter number and the name of the consumer.
name = input(("Enter your name :"))
meter_number = int(input("Enter your meter number :"))
unit = int(input("Enter your unit you can consumed :"))
if unit <= 100:
    result = unit * 4
    print(result)
elif unit <= 200:
    result = (100*4) + (unit-100) * 7
    print(result)
elif unit <= 300:
    result = (100*4) + (100*7) + (unit-200) * 12
    print(result)
else:
    result = (100*4) + (100*7) + (100*12) + (unit-300) * 16

    print("Total Bill :",result)