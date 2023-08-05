# lf i n python

# answer=input(" do you like me ? ")

# if answer == "yes" :
#     print(" well it makes me happy thank you ")

# answer=input(" do you like me ? ")

# if answer == "yes" :
#     print(" well it makes me happy thank you ")

# if answer == "no" :
#     print(" have nice day")

# ASK put condition that you must type only upper case

# pythonLover = input("what is you favorite programming language ? type upper!")

# if pythonLover.upper() == "PYTHON" :
#     print("yes that's it")
#     print("love django by the way")

# print("its ok if you love other languages")

# the last line print whether it true or false unintended print outside the condition just for showing

# pythonLover = input("what is you favorite programming language ?")

# if pythonLover.upper() == "PYTHON" :
#     print("yes that's it")
#     print("love django by the way")

# replaced upper with capitalize

# pythonLover = input("what is you favorite programming language ?")

# if pythonLover.capitalize() == "Python" :
#     print("yes that's it")
#     print("love django by the way")

# ues number
# valet = int(input("enter the value"))

# if valet > 100 :
#     print(" your are good customer ")

# hear you must convert variable from string to int so we use int or we get error

# using else

# valet = int(input("enter the value"))

# if valet > 100 :

#      print(" your are good customer ")

# else:
#     print("this your lukey day")

# using boolean =========

#  hear if you enter less 100 you get error that value is not defined because  it is boolean and only if it's true  it work

# if valet > 100 :
#     value = True

# if value :

#      print(" your are good customer ")


# so to solve problem hear we first declare variable as true and than if meet conditions it change to True


# value = False

# valet = int(input("enter the value"))

# if valet > 100 :
#     value = True

# if value :

#      print(" your are good customer ")

# else :
#     print("you money is not enough!")


# hear is challenge  if you want to calculate shipping for user

# shipping = False

# total = int(input("Enter total purchase: "))

# if total < 50:
#     total += 10
#     shipping = True

# print("Total: $" + str(total))
# if shipping:
#     print("Shipping: $10")
# else:
#     print("Shipping: Free")
# ```

# Here's how this code works:

# 1. We start by setting the `shipping` variable to `False`.

# 2. We prompt the user to enter the total purchase amount using the `input()` function and convert the input to an integer using the `int()` function.

# 3. We check if the total purchase amount is less than 50. If it is, we add 10 to the total and set the `shipping` variable to `True`.

# 4. We print the total purchase amount using the `print()` function and the `str()` function to convert the integer to a string.

# 5. We check the value of the `shipping` variable and print either "Shipping: $10" or "Shipping: Free" using the `print()` function.

# With these changes, the code should correctly calculate the total purchase amount and shipping cost based on the input and output the results to the user.

# elif

# city = input("Enter your city :")

# if city == 'shiraz':

#     print('yes you in the flower city')

# elif city == 'london':

#     print('you love sun ?')

# elif city == 'newyork' :

#     print('city never sleep')

# else  :
#     print('i am sure it\'s the best place in the world')


# and

# city = input("Enter your city :")

# street = input("Enter your street")

# if city == 'shiraz' and street == 'pezashkan' :
#     print("you are our neighbor ")

# else :
#     print("have nice day")

# or

# Use strip() method: You can use the strip() method to remove any leading or trailing spaces from the input. This can help ensure that the input is formatted correctly. Here's an example:

# python
# city = input("Enter your city: ").strip()
# street = input("Enter your street: ").strip()

# city = input("Enter your city: ").strip()
# street = input("Enter your street: ").strip()

# if city.lower() == 'shiraz'  and\
#     street.lower() == 'pezashkan' or street.lower() == 'dostan' :

#   print("You are our neighbor")
# else:
#     print("Sorry, we don't recognize your city and street.")

# out
# You are our neighbor

# hear we put prentices to divide code into two part and each evacuated separated  so if somebody type wrong street it gives the else message

# better code

# Use descriptive variable names: Instead of using generic variable names like city and street, consider using more descriptive names that convey the purpose of the variables. For example, you could use user_city and user_street.

# Prompt the user to enter their city and street
# Prompt the user to enter their city and street
# user_city = input("Enter your city: ").strip()
# user_street = input("Enter your street: ").strip()

# # Check if the user is our neighbor based on their city and street
# if user_city.lower() == 'shiraz' and (user_street.lower() == 'pezashkan' or user_street.lower() == 'dostan'):
#     print("You are our neighbor")
# else:
#     print("Sorry, we don't recognize your city and street.")
