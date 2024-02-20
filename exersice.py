#given list names = ['ram', 'shyam', 'hari', 'sita']
# print names using for and while loop
#no matter what the string length is

names = ['ram', 'shyam', 'hari', 'sita', 'Alice']

x = len(names)

for x in names:
    print(x.capitalize())

#student_grade = {'shyam': 32, 'hari': 18, 'ram': 25}
#print all the names and corresponding grde using both for loop
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
    