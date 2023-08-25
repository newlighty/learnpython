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

# import turtle
# for take in range(4):
#     turtle.backward(100)
#     turtle.right(90)
#     turtle.color('red')
#     turtle.width(5)

#  change the whole thing to red

# import turtle
# for take in range(4):
#     turtle.width(5)
#     turtle.backward(100)
#     turtle.right(90)
#     turtle.color('red')


# import tkinter as tk

# # Create a window and a canvas
# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()

# # Define the coordinates of the polygon
# coords = [100, 100, 300, 100, 300, 300, 100, 300]

# # Divide the polygon into two sub-polygons
# sub_coords1 = [coords[0], coords[1], coords[2], coords[3], coords[4], coords[5], coords[6], coords[1]]
# sub_coords2 = [coords[6], coords[1], coords[0], coords[7], coords[2], coords[3], coords[4], coords[5]]

# # Fill each sub-polygon with a different color
# canvas.create_polygon(sub_coords1, outline='black', fill='red')
# canvas.create_polygon(sub_coords2, outline='black', fill='green')

# # Start the main loop
# root.mainloop()

# nested for more complex shape

# this create one pentagon

# #import turtle
# for take in range(5):
#     turtle.forward(100)
#     turtle.right(360/5)

# this draws one pentagon and five inside of it!

# import turtle
# for take in range(5):
#     turtle.forward(100)
#     turtle.right(360/5)
#     for take1 in range(5):
#         turtle.forward(50)
#         turtle.right(360/5)

# another exp :
# import turtle
# for take in range(4):
#     turtle.forward(10)
#     turtle.right(90)
#     for take1 in range(4):
#         turtle.forward(50)
#         turtle.right(90)
#         turtle.color('green')


# To change the stroke color of the sub-polygons in the given code, you can use the `turtle.pencolor()` method in `turtle`. Here's how you can modify your code to change the stroke color of the sub-polygons:

# ```python
# import turtle

# takes = 6

# for take in range(takes):
#     turtle.forward(100)
#     turtle.right(360/takes)

#     for take1 in range(takes):
#         turtle.forward(50)
#         turtle.right(360/takes)
#         turtle.color('blue', 'green')  # Set the stroke color to blue and the fill color to green
#         turtle.begin_fill()   # Begin filling the shape
#         turtle.fillcolor('green')  # Set the fill color to green
#         turtle.end_fill()     # End filling the shape
#         turtle.pencolor('red')  # Set the stroke color to red

# turtle.done()
# ```

# In this modified code, I added the following lines:

# - `turtle.color('blue', 'green')`: This line sets the stroke color to blue and the fill color to green.
# - `turtle.pencolor('red')`: This line sets the stroke color to red after filling the sub-polygon.

# By using these lines, the sub-polygons will be filled with green color and the stroke color will be changed to red after filling each sub-polygon. You can modify the color names or use RGB values to specify different colors as needed.

# Remember to include `turtle.done()` at the end of your code to keep the turtle graphics window open.

# Citations:
# [1] https://www.geeksforgeeks.org/python-turtle-pencolor-method/
# [2] https://stackoverflow.com/questions/65968825/changing-only-fill-or-line-color-in-python-turtle
# [3] https://docs.python.org/3/library/turtle.html
# [4] https://vegibit.com/change-pen-color-in-python-turtle/
# [5] https://youtube.com/watch?v=1veDZJLsFCc
# [6] https://youtube.com/watch?v=Y_t038MLvGo
# [7] https://youtube.com/watch?v=kX4VweLMglc
# [8] https://youtube.com/watch?v=wP7dP-hY7Vk

# and her we draw enfants

# To change the shape to an elephant in `turtle`, you can use the `turtle.register_shape()` method to register a new shape for the turtle. Here's an example code snippet that demonstrates how to change the shape to an elephant:

# ```python
# import turtle

# # Register the elephant shape
# turtle.register_shape("elephant", ((50,-50),(50,-25),(25,-25),(25,0),(50,0),(50,25),(0,25),(0,50),(-50,50),(-50,25),(-25,25),(-25,0),(-50,0),(-50,-25),(0,-25),(0,-50)))

# # Set the turtle shape to elephant
# turtle.shape("elephant")

# # Move the turtle forward
# turtle.forward(100)

# turtle.done()
# ```

# In this code, I used the `turtle.register_shape()` method to register a new shape for the turtle. The `register_shape()` method takes two arguments: the name of the new shape and a tuple of coordinates that define the shape. In this example, I defined the coordinates of an elephant shape and registered it with the name "elephant".

# After registering the new shape, I used the `turtle.shape()` method to set the turtle shape to "elephant". Finally, I moved the turtle forward to demonstrate the new shape.

# Remember to include `turtle.done()` at the end of your code to keep the turtle graphics window open.

# Citations:
# [1] https://stackoverflow.com/questions/50052835/python-turtle-shapes
# [2] https://www.geeksforgeeks.org/turtle-color-method-in-python/
# [3] https://docs.python.org/3/library/turtle.html
# [4] https://python-forum.io/thread-14362.html
# [5] https://vegibit.com/change-pen-color-in-python-turtle/
# [6] https://www.geeksforgeeks.org/python-turtle-pencolor-method/


# add gradient to the shape

# import turtle

# Register the elephant shape
# turtle.register_shape("elephant", ((50,-50),(50,-25),(25,-25),(25,0),(50,0),(50,25),(0,25),(0,50),(-50,50),(-50,25),(-25,25),(-25,0),(-50,0),(-50,-25),(0,-25),(0,-50)))

# # Set the turtle shape to elephant
# turtle.shape("elephant")

# # Set the gradient colors
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# for i in range(len(colors)):
#     turtle.color(colors[i], colors[i-1])
#     turtle.begin_fill()
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.end_fill()

# turtle.done()


# import turtle

# # Register the shape
# turtle.register_shape("my_shape", ((-50, -50), (50, -50), (50, 50), (-50, 50)))

# # Set the turtle shape to the registered shape
# turtle.shape("my_shape")

# # Set the gradient colors
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# for i in range(len(colors)):
#     turtle.color(colors[i], colors[i-1])
#     turtle.begin_fill()
#     turtle.circle(50)
#     turtle.end_fill()

# turtle.done()

# ----------------
# we can specify that loop start from 1 not 0 and give it stop number 10 and scape number 2 means it add two to the one
# 1 + 2 = 3 3+2 = 5 and this is output :

# 1
# 3
# 5
# 7
# 9

# for count in range(1,10,2):
# print(count)

# and this way you can specify what you want :
# for count in [1,2,3,4,5]:
#     print(count)

# and hear not use for just with numbers

# import turtle
# for steps in ['red', 'blue', 'green', 'yellow']:
#     turtle.color(steps)
#     turtle.forward(100)
#     turtle.right(90)

# challenge drave octagon with octagons in it

# import turtle
# takes  = 8
# for take in range(takes):
#     turtle.forward(100)
#     turtle.right(360/takes)
#     for take1 in range(takes):
#         turtle.forward(50)
#         turtle.right(360/takes)

# turtle.done()

# and this one ask user to tell the number of sides :

# import turtle
# takes = int(input("enter your side !"))

# for take in range(takes):
#     turtle.forward(100)
#     turtle.right(360/takes)
#     for take1 in range(takes):
#         turtle.forward(50)
#         turtle.right(360/takes)

# turtle.done()

#  your going to love this one
# import turtle
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         turtle.color(c)
#         turtle.forward(steps)
#         turtle.right(30)


# turtle.done()

# #import turtle
# for steps in range(100):
#     for c in ('blue', 'red', 'green', 'purple'):
#         turtle.color(c)
#         turtle.forward(steps)
#         turtle.right(30)


# turtle.done()

# Exercise 1: Calculate the multiplication
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# number1 = 20
# number2 = 30
# Expected Output:

# The result is 600
# number1 = 20
# number2 = 30
# number1 = int(input('enter your number'))
# number2 = int(input('enter your number'))
# total = number1 * number2
# print(total)
# if total < 1000 :
#     print('you can return goods')
# else:
#     print(total)


# number1 = 40
# number2 = 30

# The result is 70

# number1 = 20
# number2 = 30
# number1 = int(input('enter your number'))
# number2 = int(input('enter your number'))
# total = number1 + number2
# print(total)
# if total < 1000 :
#     print('you can return goods')
# else:
#     print(total)

# while loop used when you want so action repeat but you dont know fo how many  like enter your password of print user name or ..etc

# answer = '0'

# while answer !='frank':
#     answer = input('frank')
# print('welcome to your dashboard')

# import turtle
# counter = 0
# while counter < 4 :
#     turtle.forward(100)
#     turtle.right(90)
#     counter = counter+1
# turtle.done()
#
#  look at this code and tell what is add

# import turtle
# counter = 0
# while counter < 20 :
#     turtle.forward(100)
#     turtle.right(90)
#     counter = counter+1
#     print(counter)
# turtle.done()

# help !

# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# =========================>

# In the given code, the counter starts from 0, but when it is printed, it starts from 1. This is because the `print(counter)` statement is placed after the line `counter = counter + 1`.

# Here's a breakdown of the code execution:

# 1. The `counter` variable is initialized to 0.
# 2. The while loop is executed as long as the `counter` is less than 20.
# 3. Inside the loop, the turtle moves forward by 100 units and then turns right by 90 degrees.
# 4. The `counter` is incremented by 1 using the statement `counter = counter + 1`.
# 5. After the increment, the value of `counter` is printed using `print(counter)`.
# 6. The loop continues until the `counter` reaches 20.
# 7. Finally, the `turtle.done()` function is called to finish the turtle graphics.

# Since the `counter` is incremented before printing, the first value printed is 1. If you want the counter to start from 0 when printing, you can move the `print(counter)` statement before the line `counter = counter + 1`. Here's the modified code:

# ```python
# import turtle

# counter = 0
# while counter < 20:
#     turtle.forward(100)
#     turtle.right(90)
#     print(counter)
#     counter = counter + 1

# turtle.done()
# ```

# Now, when you run the code, the counter will start from 0 when printed.


# output

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19

# Citations:
# [1] https://www.pythonclassroom.com/turtle-graphics/turtle-graphics-with-loops
# [2] https://realpython.com/beginners-guide-python-turtle/
# [3] https://quizlet.com/427915829/tracy-the-turtle-unit-1-computer-science-flash-cards/
# [4] https://artofproblemsolving.com/assets/pythonbook/hello_little_turtles.html
# [5] http://opensask.ca/Python/Overview/MultipleTurtlesAndForLoops.html
# [6] https://www.cs.cornell.edu/courses/cs1110/2015fa/assignments/assignment4/index.php

# how to make for loop for ever
# import turtle

# counter = 0
# while True:
#     turtle.forward(100)
#     turtle.right(90)
#     print(counter)
#     counter = counter + 1

# turtle.done()

# hear is another way around it

# import turtle
# counter = 0
# while counter < 3 :
#     turtle.forward(100)
#     turtle.right(90)


# ========================= list==================

# guests = ['frank','rose', 'jack','lucy']
# print(guests[-2])

# you can change the value of the list :

# guests = ['frank','rose', 'jack','lucy']
# guests[3] = 'nanny'
# print(guests[3])

# another way to do this is using append() and new value added to the end of te list no need for tell where to put it

# guests = ['frank','rose', 'jack','lucy']
# guests.append('faramarz')
# print(guests[4])

# how to print all the the list value ?
#  oyu can use for loop for this

# guests = ['frank','rose', 'jack','lucy']
# for guest in guests:
#     print(guest)

# guests = ['frank','rose', 'jack','lucy']
# for guest in guests:
#     print(guest)

# an in case you do'nt know how many gust is going to add you van use while loop

# guests = ['frank', 'rose', 'jack', 'lucy']
# index = 0
# while index < len(guests):
#     print(guests[index])
#     index += 1
# remove()

# guests = ['frank', 'rose', 'jack', 'lucy']
# guests.remove('frank')
# print(guests)

# another way of doing this :
# guests = ['frank', 'rose', 'jack', 'lucy']
# del guests[0]
# print(guests)

# how to search list
# guests = ['frank', 'rose', 'jack', 'lucy']
# print(guests.index('rose'))
#  first know the length of list and than print it
# guests = ['frank', 'rose', 'jack', 'lucy']
# for guest in range(len(guests)):
#   print(guests[guest])
#  and this is how to sort things :

# guests = ['frank', 'rose', 'jack', 'lucy']
# guests.sort()
# for guest in guests:
#   print([guest])

# guests = ['frank', 'rose', 'jack', 'lucy']
# guests.sort()
# for guest in guests:
#   print(guest)
