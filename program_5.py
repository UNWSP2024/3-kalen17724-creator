# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
hot_dog = 3.50
chili_dog = 4.50 
cheese = 0.50
peppers = 0.75 
grilled_onions = 1
tax_rate= 0.07

dog_choice = input("What type of dog would you like? hot dog or chili dog: ")
if dog_choice =="hot dog": 
    cost = hot_dog
elif dog_choice =="chili dog":
    cost = chili_dog
else:
    print ("**Invalid Choice** default is hot dog")
    cost = hot_dog

toppings = input("Any toppins? cheese, peppers, or grilled onions: ")

if "cheese" in toppings:
    cost += cheese
if "peppers" in toppings:
    cost += peppers
if "grilled onions" in toppings:
    cost += grilled_onions
else:
    print ("invalid response, no toppings.")

tax = cost * tax_rate
total = cost + tax 

print (f"Order total: ${cost:.2f}")
print (f"tax: ${tax:.2f}")
print (f"toatl cost: ${total:.2f}")
