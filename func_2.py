#-------------------------------------Write a function that takes a string and returns the length of the string and display it-------------------------------------------------
 
# def string_length(text):
#     length = len(text)
#     return length
# string = input("Enter a string : ")
# print(string_length(string))





# --------------------------------------------Write a function that takes a string and prints the length of the string.-------------------------------------------------------------
# def string_length(text):
#     length = len(text)
#     print(length)
# string = input("Enter a string : ")
# string_length(string)





# ----------------------------------Write a function that takes a string and returns and display the first alphabet of the string-----------------------------------------------------

#------------------------------------------------using for loop--------------------------------------------------------------------------------------------------------------------
# def first_alpha(text):
#     for char in text:
#         return char

# f_alpha = first_alpha("Hello")
# print(f_alpha)
#------------------------------------------Using Index-------------------------------------------------------------------------------------------------------
# def first_alpha(text):
#         return text[0]

# f_alpha = first_alpha("Hello")
# print(f_alpha)





# ---------------------Write a function that takes a number and returns True if the number is even and returns False if the number is odd------------------------------

# def check():
#     num = int(input("Enter a number: "))

#     if num % 2 == 0:
#         return True    
#     else:
#         return False

# print(check())





#----------------------------------------------------- Write a function that takes a number and print wether that number is odd or even.-------------------------------------------
    # 2 --> 2 is even
    # 3 --> 3 is odd

# def check_2(num):
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")

# num = int(input("Enter a number : "))
# check_2(num)




# -------------------------------------------Write a function that takes a string and returns the reverse of the string.-----------------------------------

#------------------------------------------------------------------------- Using Loop
# def reverse(text):
#     result = ""
#     for char in text:
#         result = char + result
    
#     return result

# text = input("Enter a string : ")

# print(reverse(text))



#----------------------------------------------------------------------------using slicing

# def rev_text(text):
#     reversed_text = text[-1::-1]
#     print(f"Original String : {text}")
#     print(f"Reversed String : {reversed_text}")

# text = input("Enter a string : ")

# rev_text(text)





# -----------------------------------------Write a function that takes a string and returns the lower case string--------------------------------------------

# def lower(text):
#     lower_string = text.lower()
#     return lower_string

# text = input("Enter a sting : ")

# l_string = lower(text)
# print(l_string)

#----------------------------------------------------------------Returning only lower string-----------------------------------------------------------------------

# def only_lower(text):
#     lower_string = ''.join(char for char in text if char.islower())
#     return lower_string

# text = input("Enter a string : ")

# lower = only_lower(text)
# print(lower)



# --------------------------------------Write a function that takes a string and count the number of the letter u present in the string.---------------------------------

# def count_u(text):
#     count = text.count('u')
#     return count

# text = "Unveiling unique underwater universes, Ulysses, an underwater explorer, uncovered unimaginable umbrella-shaped undersea formations."
# print(count_u(text))





#-----------------------------Write a function that takes a string and count the number of the letter u present in the string diresgarding case sensitivity.---------------

# def count_letter(text):
#     lower = text.lower()
#     count = lower.count('u')
#     return count

# text = input("Enter a string : ")
# print(count_letter(text))




#-------------------------------------------- Write a function that takes a string and returns the last aplhabet of the string.--------------------------------------


# def last_alpha(input_string):
#     reversed_text = input_string[::-1]
#     for char in reversed_text:
#         if char.isalpha():
#             return char
#         else:
#             return None

# string = "Hello World"
# print(last_alpha(string))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def last_alpha(input_string):
#     return input_string[-1]

# string = input("Enter a string : ")
# l_alpha = last_alpha(string)
# print(l_alpha)





#------------------------------------ Write a function that takes a number and returns the list of even numbers upto that number.---------------------------------------

# ---------------------------------------------------------Using For Loop-------------------------------------------------------------------------------------------------
# def even(num):
#     check_num = range(0, num + 1)
#     even_num = []

#     for i in check_num:
#         if i % 2 == 0:
#             even_num.append(i)
#     print(even_num)    

# num = int(input("Enter a number : "))
# even(num)

# ------------------------------------------------------Using List Comprehension------------------------------------------------------------------------------------------

# def even(num_limit):
#     even_numbers = [num for num in range(2, num_limit + 1) if num % 2 == 0]
#     return even_numbers

# num = int(input("Enter a number : "))

# even_num = even(num)
# print(even_num) 




# ----------------------------------------------------Write a function that takes a list of numbers and returns the list of even numbers.--------------------------------------

# def even(num_list):
#     e_num = [num for num in num_list if num % 2 == 0]
#     return e_num
# num = [0, 1, 2, 3, 4, 5, 675, 888, 9999, 17283]

# result = even(num)
# print(result)





# -------------------------------------------Write a funciton that takes  a list of numbers and returns the list of odd numbers.

# def odd(num_list):
#     o_num = [num for num in num_list if num % 2 != 0]
#     return o_num

# num = [1, 3, 6, 555, 5000, 35479, 78]
# result = odd(num)
# print(result)




# ---------------------------Write a funciton that takes a list of numbers and returns the list of odd and even numbers.----------------------------------------------------

# def o_e_num(num_list):
#     e_num = [num for num in num_list if num % 2 == 0]
#     o_num = [num for num in num_list if num % 2 != 0]
    
#     return e_num, o_num

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 33, 44, 23, 66]
# even_result, odd_result = o_e_num(num)
# print(f"Even list : {even_result}")
# print(f"Odd list : {odd_result}")


# ----------------------------------Write a function that takes a string and returns the first vowel present in the string.---------------------------------------------------

# def check_vowel(input_string):
#     for char in input_string:
#         if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#             return char
        

# string = input("Enter a string : ")
# result = check_vowel(string)
# print(result)


# def check_vowel(input_string):
#     vowels = 'aeiouAEIOU'
#     for char in input_string:
#         if char in vowels:
#             return char
#     return None
        

# string = input("Enter a string : ")
# result = check_vowel(string)
# print(result)



#-------------------------------- Write a function that takes a string and returns the first consonant present in the string.-----------------------------------------------

    # def check_consonant(input_string):
    #     vowels = 'aeiouAEIOU'
    #     for char in input_string:
    #         if char not in vowels:
    #             return char
    #     return None
            

    # string = input("Enter a string : ")
    # result = check_consonant(string)
    # print(result)



# -----------------------------Write a function that takes a string and returns the total number of vowels present inthe string-------------------------------------------------

# def count_vowels(text):
#     lower = text.lower()
#     vowels = 'aeiou'
#     count = 0

#     for char in lower:
#         if char in vowels:
#             count = count + 1

#     return count

# input_text = input("Enter text : ")
# print(count_vowels(input_text))


# ------------------------------Write a function that takes a string and returns the total number of consonants present inthe string-----------------------------------------------

# def count_const(text):
#     text_lower = text.lower()
#     vowels = 'aeiou'
#     count = 0

#     for char in text_lower:
#         if char not in vowels:
#             count = count + 1
        
#     return count

# input_text = input("Enter text : ")
# result = count_const(input_text)
# print(result)




#----------------- Write a function that takes a string and returns the total number of vowels and consonants present inthe string in dictionary format.-------------------------

def count_vc(text):
    l_text = text.lower()
    vowels = 'aeiou'
    count = {'vowels' : 0, 'constant' : 0}

    for char in text:
        if char.isalpha():
            if char in vowels:
                count['vowels'] += 1
            else:
                count['constant'] += 1
    
    return count

input_text = input("Enter a text : ")
result = count_vc(input_text)

print(result)
