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



#-------------- Write a function that takes a date in format '1994-05-15' or '1994/05/15'
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

#--------------- Write a function that takes a number and returns even number upto that number.

#num ----> user input
#range ----> 2 to num+1
#if num in range % 2 == 0
#empty list even num
#print even num

# def check_even(num):
#     num_list = range(2, num + 1)
#     even_num = []

#     for n in num_list:
#         if n % 2 == 0:
#             even_num.append(n)
    
#     return even_num

# input_num = int(input("Enter a number : "))
# e_num = check_even(input_num)
# print(e_num)


#------------------- write a function that takes an email and check wether that email belongs to edu.np account or not.

# def check_email(email):
#     if '.edu.np' in email:
#         print("Email belongs to .edu.np")
#     else:
#         print("Email doesnot belong to .edu.np")

# input_email = input("Enter your Email : ")
# check_email(input_email)

#-------------------- write a function that takes a number and count the sum of numbers upto that number.

# def num_sum(num):
#     num_list = range(0, num + 1)
#     sum = 0

#     for i in num_list:
#         sum = sum + i

#     return sum

# n = int(input("Enter a number : "))
# list = num_sum(n)
# print(list)


# ----------------write a function that takes a number and count the product of numbers upto that number.

# def num_product(num):
#     num_list = range(1, num+1)
#     product = 1

#     for i in num_list:
#         product = product * i

#     return product

# n = int(input("Enter a number : "))

# p_num = num_product(n)

# print(p_num)



#----------------------------- write a function that takes 4 numbers and returns the sum of those number

#------> Passing indivudal arguments

# def sum_num(num_1, num_2, num_3, num_4):
#     sum = num_1 + num_2 + num_3 + num_4
#     return sum

# #Positional arguments
# print(sum_num(1, 2, 3, 4))  
# #Keyword arguments
# print(sum_num(num_1 = 1, num_4 = 2, num_3 = 3, num_2 = 4))  
# #-------> Taking user_input
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))
# num4 = int(input("Enter fourth number : "))

# sum = sum_num(num1, num2, num3, num4)
# print(sum)

#------->using *args
#Using *args

user_input = input("Enter number separated by spaces : ")
user_number = user_input.split()\
num1, num2, num3, num4 










