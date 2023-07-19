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
