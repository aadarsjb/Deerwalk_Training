# write a function that takes a string and check if that string is paldinrome or not disegrading case sensitivity.
# hannah, mom, dad, racecar

# def check_palindrome(s):
#     l_s = s.lower()
#     rev_text = l_s[::-1]

#     if rev_text == l_s:
#         print(f"{s} is palindrome")
    
#     else:
#         print(f"{s} is not palindrome")

# user_input = input("Enter a word : ")
# check_palindrome(user_input)



# Write a function that takes a date in format '1994-05-15' or '1994/05/15'
# and return in dicntioary
# {'year': '1994', 'month': '05', 'day': '15'}

# def print_date(i_date):
#     #split the date
#     if '-' in i_date:
#         split_date = i_date.split('-')
#     elif '/' in i_date:
#         split_date = i_date.split('/')
#     else:
#         print("Invalid Date Format!")

#     #Extracting indiviuals
#     year, month, day = split_date

#     #storing in dict
#     date_dict = {'year': year, 'month': month, 'day': day}
#     return date_dict


# input_date = input('Enter date separated by "/" or "-" : ')

# print(print_date(input_date))


        

