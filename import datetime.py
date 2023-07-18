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
