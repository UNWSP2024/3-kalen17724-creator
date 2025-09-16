# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".
infant = 1
child = range(2, 12)
teenager = range(13, 19)
adult = range(20, 150)


age= int(input("Enter age: "))
     
if age ==infant:
    print("infant")
elif age in child: 
    print("child")
elif age in teenager:
    print("teenager")
elif age in adult:
    print("adult")
else: 
    print ("invalid age")
