# school = 'Deerwalk Institute of Technology'
# slce deerwalk only
# slice institute only
# slice Technology only
# check if tehnology exists in the variable school regarding case sensetive
# 'technology' in school
# check the len of the str
# check if the string contains the letter i or I
# count the number of the letter i or I 



school = "Deerwalk Institute Of Technology"

print('Slicing "Deerwalk"')
x = school[:8]
print(x)

print(" ")

print('Slicing "Institute"')
x = school[9:18]
print(x)

print(" ")

print('Slicing "Technology"')
x = school[22:]
print(x)

print(" ")
print("'technology' in school")
print('technology' in school)

print(" ")

substring_to_check = 'technology'

if substring_to_check in school:
    print(f'"{substring_to_check}" exists in the variable "school".')
else:
    print(f'"{substring_to_check}" does not exist in the variable "school".')

print(" ")
print(f'Length of the string: {len(school)}')

print(" ")
print("check if the string contains the letter i or I:")
print('i' in school)
print('I' in school)
#converts it to lowercase (char.lower()), and then checks if it is equal to the lowercase 'i'.
print(any(char.lower() == 'i' for char in school))

print(" ")

print("count the number of the letter i or I :")
print(school.lower().count('i'))

