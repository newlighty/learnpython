# import datetime

# current  = datetime.datetime.now()


# this is how you can show formatted date in persian
# from persiantools.jdatetime import JalaliDateTime


# for run this use run in current interactive mode in debug
# from persiantools.jdatetime import JalaliDateTime
# jalali_datetime = JalaliDateTime.today()

# formatted_datetime = jalali_datetime.strftime("%Y-%m-%B-%d %H:%M")

# print(formatted_datetime)


# how to calculate birthay of someone

# from persiantools.jdatetime import JalaliDateTime

# # Get the current Jalali date and time
# jalali_datetime = JalaliDateTime.now()

# formatted_datetime = jalali_datetime.strftime("%Y-%m-%B-%d %H:%M")

# # Create a JalaliDateTime object for Mahsa's birthday
# mahsa_birthday = JalaliDateTime(1402, 5, 2)

# # Calculate the number of days until Mahsa's birthday
# days_until_birthday = (mahsa_birthday - jalali_datetime).days

# # Print the number of days until Mahsa's birthday
# print("Days until Mahsa's birthday:", days_until_birthday, formatted_datetime)

# from persiantools.jdatetime import JalaliDateTime

# jalali_datetime = JalaliDateTime.now()

# formatted_datetime = jalali_datetime.strftime("%Y-%B-%A")

# print(formatted_datetime)
# out put  1402-Tir-Chaharshanbeh

# this one get back persian output date time

# from persiantools.jdatetime import JalaliDateTime

# # Get the current Jalali date and time
# jalali_datetime = JalaliDateTime.now()

# # Define the Farsi month and day names
# farsi_months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
# farsi_days = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه']

# # Format the JalaliDateTime object using Farsi month and day names
# formatted_datetime = f"{jalali_datetime.year} {farsi_months[jalali_datetime.month-1]} {farsi_days[jalali_datetime.weekday()]}"

# # Print the formatted datetime
# print(formatted_datetime)

# output  1402 تیر چهارشنبه

# In the example above, we first import the `JalaliDateTime` class from the `persiantools.jdatetime` module and create a `JalaliDateTime` object for the current date and time using `JalaliDateTime.now()`.

# We then define two lists, `farsi_months` and `farsi_days`, that contain the Farsi names for the months and days of the week, respectively.

# Finally, we format the `JalaliDateTime` object using the Farsi month and day names and print the formatted datetime.

# Note that we use the `weekday()` method of the `JalaliDateTime` object to get the day of the week as an integer (0 for Monday, 1 for Tuesday, etc.), and use that integer to index into the `farsi_days` list to get the corresponding Farsi day name.

# this one output is english date to persian language

# import datetime

# # Get the current date and time
# current = datetime.datetime.now()

# # Format the datetime object using strftime() with Farsi format
# formatted_datetime = current.strftime("%Y-%B-%A-%d").replace("January", "ژانویه").replace("February", "فوریه").replace("March", "مارس").replace("April", "آوریل").replace("May", "مه").replace("June", "ژوئن").replace("July", "جولای").replace("August", "اوت").replace("September", "سپتامبر").replace("October", "اکتبر").replace("November", "نوامبر").replace("December", "دسامبر").replace("Saturday", "شنبه").replace("Sunday", "یکشنبه").replace("Monday", "دوشنبه").replace("Tuesday", "سه‌شنبه").replace("Wednesday", "چهارشنبه").replace("Thursday", "پنج‌شنبه").replace("Friday", "جمعه")

# # Print the formatted datetime
# print(formatted_datetime)

# 2023-جولای-چهارشنبه-19

# and the last one show persian date month and day full
# from persiantools.jdatetime import JalaliDateTime add day dight

# # Get the current Jalali date and time
# jalali_datetime = JalaliDateTime.now()

# # Define the Farsi month and day names
# farsi_months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
# farsi_days = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه']

# # Format the JalaliDateTime object using Farsi month and day names
# formatted_datetime = f"{jalali_datetime.year} {farsi_months[jalali_datetime.month-1]} {farsi_days[jalali_datetime.weekday()]} {jalali_datetime.day}"

# # Print the formatted datetime
# print(formatted_datetime)

# output  1402 تیر چهارشنبه 28


# If you want to use alternate parameters for the Farsi month and day names, you can define your own lists of names and use them in the formatting. Here's an example:

# ```python
# from persiantools.jdatetime import JalaliDateTime

# # Get the current Jalali date and time
# jalali_datetime = JalaliDateTime.now()

# # Define alternate Farsi month and day names
# alternate_farsi_months = ['ماه ۱', 'ماه ۲', 'ماه ۳', 'ماه ۴', 'ماه ۵', 'ماه ۶', 'ماه ۷', 'ماه ۸', 'ماه ۹', 'ماه ۱۰', 'ماه ۱۱', 'ماه ۱۲']
# alternate_farsi_days = ['روز ۱', 'روز ۲', 'روز ۳', 'روز ۴', 'روز ۵', 'روز ۶', 'روز ۷']

# # Format the JalaliDateTime object using alternate Farsi month and day names
# formatted_datetime = f"{jalali_datetime.year} {alternate_farsi_months[jalali_datetime.month-1]} {alternate_farsi_days[jalali_datetime.weekday()]} {jalali_datetime.day}"

# # Print the formatted datetime
# print(formatted_datetime)
# ```

# In this example, we define `alternate_farsi_months` and `alternate_farsi_days` lists with your desired alternate Farsi month and day names.

# Then, we format the `JalaliDateTime` object using these alternate names by indexing into the lists based on the month and day values of the `JalaliDateTime` object.

# Finally, we print the formatted datetime.

# Feel free to customize the `alternate_farsi_months` and `alternate_farsi_days` lists with your preferred names.

# output 1402 ماه ۴ روز ۶ 29
