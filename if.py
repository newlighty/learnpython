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

# To make the code cleaner, you can simplify the logic and remove unnecessary variable assignments. Here's the modified code:

# ```python
# # Prompt the user to enter their city and street
# city = input("Enter your city: ").strip()
# street = input("Enter your street: ").strip()

# # Check if the user is our neighbor based on their city and street
# if city.lower() == 'shiraz' and (street.lower() == 'pezashkan' or street.lower() == 'dostan'):
#     print("You are our neighbor")
# else:
#     print("Sorry, we don't recognize your city and street.")
# ```

# In this code, the changes made include:

# - Removed unnecessary variable assignments (`city = False` and `street = False`).
# - Simplified the `if` condition by directly checking if the city is "shiraz" and the street is either "pezashkan" or "dostan".
# - Used the `lower()` method to convert the input to lowercase before comparison, ensuring case-insensitive matching.
# - Adjusted the indentation for better readability.

# These modifications make the code cleaner and more concise while maintaining its functionality.

# Citations:
# [1] http://computing.outwood.com/NEA/python/programming.html
# [2] https://towardsdatascience.com/transform-messy-address-into-clean-data-effortlessly-using-geopy-and-python-d3f726461225
# [3] https://www.programiz.com/python-programming/if-elif-else
# [4] https://www.idtech.com/blog/what-does-elif-mean-in-python
# [5] https://www.reddit.com/r/koreatravel/comments/up99b7/qcode_cannot_input_addres/
# [6] https://www.simplilearn.com/tutorials/python-tutorial/python-if-else-statement


# chalenge

# To calculate the total charge for an order from an online store in Canada, you can follow these steps:

# 1. Prompt the user to enter their country and order total:
#    ```python
#    country = input("Enter your country: ")
#    order_total = float(input("Enter your order total: "))
#    ```

# 2. Check if the user is from Canada:
#    ```python
#    if country.lower() == 'canada':
#        province = input("Enter your province: ")
#        # Calculate tax based on the province
#        # Use the appropriate tax rate for the province
#        # You can refer to the official government sources or tax calculators to get the tax rates for each province
#        # Apply the tax rate to the order total to calculate the tax amount
#        # Add the tax amount to the order total to get the total charge
#        # Print the total charge
#    else:
#        # If the user is not from Canada, do not charge any taxes
#        # The total charge will be the same as the order total
#        # Print the total charge
#    ```

# 3. Calculate tax based on the province (if applicable):
#    - You can refer to official government sources or tax calculators to get the tax rates for each province in Canada. For example, you can use the GST/HST calculator provided by the Canada Revenue Agency[2].
#    - Apply the tax rate to the order total to calculate the tax amount.
#    - Add the tax amount to the order total to get the total charge.

# Here's an example of how the code could be structured:

# ```python
# # Prompt the user to enter their country and order total
# country = input("Enter your country: ")
# order_total = float(input("Enter your order total: "))

# # Check if the user is from Canada
# if country.lower() == 'canada':
#     province = input("Enter your province: ")
#     # Calculate tax based on the province
#     # Apply the appropriate tax rate to the order total
#     # Add the tax amount to the order total to get the total charge
#     # Print the total charge
# else:
#     # If the user is not from Canada, do not charge any taxes
#     # The total charge will be the same as the order total
#     # Print the total charge
# ```

# Please note that the code provided is a template and you will need to fill in the specific tax rates and calculations based on the province. You can refer to official government sources or tax calculators to get the accurate tax rates for each province in Canada.

# Citations:
# [1] https://www.retailcouncil.org/resources/quick-facts/sales-tax-rates-by-province/
# [2] https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html
# [3] https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html
# [4] https://www.canada.ca/en/revenue-agency/services/child-family-benefits/goods-services-tax-harmonized-sales-tax-gst-hst-credit/gst-hst-credit-calculation-sheets.html
# [5] https://en.wikipedia.org/wiki/Sales_taxes_in_Canada
# [6] https://wowa.ca/calculators/gst-hst-calculator
# [7] https://www.avalara.com/vatlive/en/country-guides/north-america/canada/canadian-vat-compliance-and-rates.html
# [8] https://www.calculconversion.com/sales-tax-calculator-hst-gst.html
# [9] https://help.shopify.com/en/manual/taxes/canada/canada-tax-reference
# [10] https://hardbacon.ca/en/calculator/canadian-sales-tax-gst-pst/
# [11] https://www.taxtips.ca/salestaxes/sales-tax-rates-2022.htm
# [12] https://www.remitbee.com/gst-hst-calculator
# [13] https://empirecpa.ca/canadian-sales-tax-rates-for-2022/
# [14] https://captaincalculator.com/financial/tax/gst-canada/
# [15] https://taxsummaries.pwc.com/canada/corporate/other-taxes
# [16] https://gstcalculator.ca


# city = input("Enter your city: ").strip()
# street = input("Enter your street: ").strip()

# city = False
# if city == 'shiraz':
#     city = True

# street = False
# if street == 'pezashkan' or street == 'dostan':
#     street = True
# if city and street:
#     print("You are our neighbor")
# print("do you like coffee")

# enf of if =================

# use turtle library to draw shapes
# import turtle
# turtle.forward(150)

# import turtle
# turtle.color('green')
# turtle.forward(100)
# turtle.right(45)
# turtle.color('blue')
# turtle.forward(50)
# turtle.right(45)
# turtle.color('pink')
# turtle.forward(100)

#  for (loop) we can you this command to repeat a command in number of time we need

#  hear we made square with repeat the command for times for is keyword take is variable  in is part of syntax and range is number of time need to repeat and stop

# import turtle
# for take in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.color('green')


# import turtle
# for take in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.color('green')
#     turtle.forward(200)
