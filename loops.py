# if 3 > 2:
#     print("hello")
# elif 8 > 3:
#     print("good morning")
# else:
#     print("Afternoon")


# age = int(input("Enter your age:"))

# if age >= 5 and age <= 9:
#     print("You are young")
# elif age >=10 and age <= 19:
#     print("You are a teen")
# else:
#     print("You are Old")


# #short hand if
    

if 2 % 2 == 0:
    a = 'even'

a = 'even' if 2 % 2 == 0 else 'odd'


num = int(input('Enter a number: '))

print("The given number is even") if num % 2 == 0 else print("It is odd")

string = str(input("Enter your name: "))

x = len(string)

print(f"Length of your name is {x}")



user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"

if any(char in vowels for char in user_input):
    print("The string contains vowels")
else:
    print("Vowels are not presented  the string")

ram = 85
shyam = 72
hari = 55
rita = 22

name = str(input("Enter your first name: "))

name_lower = name.lower()

if name_lower == "ram":
    print(f"Hey Ram! You distinction grade is {ram}")
elif name_lower == "shyam":
    print(f"Hi Shyam! Your first division grade is {shyam}")
elif name_lower == "hari":
    print(f"Hi Hari! Your second division grade is {hari}")
elif name_lower == "rita":
    print(f"Hi Rita, Mom's flying chappal received at {rita}km/hr") 
else:
    print("You don't exists")

s = input('Enter a string').lower()
if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
    print("Vowel is present")
else:
    print("Vowels is not present")