# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

# option 1, 2 pounds or less
# option 2, over 2 lb less then 6lb
# option 3, over 6 and not more then 10 lb 
# option 4, over 10 lb
option_1 = 1.50
option_2 = 3.00
option_3 = 4.00
option_4 = 4.75


weight = float(input("Enter the package weight: "))

if weight >0 and weight <= 2:
    print (f"Your cost is ${weight*option_1:.2f}")
if weight >2 and weight <= 6:
    print (f"Your cost is ${weight*option_2:.2f}")
if weight >6 and weight <=10:
    print (f"Your cost is ${weight*option_3:.2f}")
if weight >10:
    print (f"Your cost is ${weight*option_4:.2f}")


