#given list names = ['ram', 'shyam', 'hari', 'sita']
# print names using for and while loop
#no matter what the string length is

names = ['ram', 'shyam', 'hari', 'sita', 'Alice']

x = len(names)

for x in names:
    print(x.capitalize())

#student_grade = {'shyam': 32, 'hari': 18, 'ram': 25}
#print all the names and corresponding grde using for loop
#Hi Shyam, Your grade is 32
    
student_grade = {
    'shyam': 32,
    'hari': 18,
    'ram': 25
    }

grade = student_grade.items()

for x in grade:
    print(x)

#print even numbers from 2 to 30 including 30
num = range(2, 31, 2)
for x in num:
    print(x)

#student_grade = {'shyam': 32, 'hari': 18, 'ram': 25}
#print all the names and corresponding grade
#Hi Shyam, Your grade is 32


students_grade = {
    "shyam" : 35,
    "hari" : 18,
    "ram" : 25
}
# creates an infinite loop in Python

for name, grade in students_grade.items():
    print(f"Hi {name.capitalize()}!, Your grade is {grade}")
   
#crete a list from 2 to 50
#separate odd and even number from the list into separate list
# even_list
#odd_list
    
num_list = list(range(2, 51))

print(f"Original List : {num_list}")

even_list = [num for num in num_list if num % 2 == 0]
odd_list = [num for num in num_list if num % 2 != 0]

print(f"Even List : {even_list}")
print(f"Odd List : {odd_list}")

#use break continue to run the program without stopping
# enter 0 to exit 1 to continue

num = int(input("Multiple of : "))
i = 0
while i <= 2:
    print(num * i)  
    i = i + 1

    num_1 = int(input("Enter 1 to continue, 0 to exit : "))
    if num_1 == 0:
        break
    elif num_1 ==1:
        continue
    else:
        print("Invalid choice")
        break

#--------------Checking Student Grade -----------------
    
student_grade = {
    "ram" : 85,
    "shyam" : 72,
    "hari" : 55,
    "rita" : 22
}


while True:
    name = input("Enter your name : ")
    name_lower = name.lower()

    if name_lower in student_grade:
        grade = student_grade[name_lower]

        if grade >= 75:
            print(f"Hi {name_lower.capitalize()}!, You Distinction grade is {grade}")

        elif grade >= 60:
            print(f"Hi {name_lower.capitalize()}!, You First Divison grade is {grade}")                

        elif grade >= 45:
            print(f"Hi {name_lower.capitalize()}!, You Distinction grade is {grade}")    

        else:
            print(f"Hi {name_lower.capitalize()}!, Mom's flying chapal received at {grade}km/hr")            

        choice = input("Enter 0 to exit, 1 to continue : ")
        if choice == '0':
            break
        elif choice == '1':
            continue
        else:
            print("Invalid Choice")
            break
    else:
        print("Invalid Name")    




    