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
