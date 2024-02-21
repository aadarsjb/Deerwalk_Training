#------> Positional argument
def info(fn, ln, age):
    print(f"Hi {fn} {ln}. You are {age} yers old.")

info("Kurt", "Cobain", "27")

#------> Keyword argument
info(age = 27, ln = "Cobain", fn = "Kurt")



# student_grade = {
#     "ram" : 85,
#     "shyam" : 72,
#     "hari" : 55,
#     "rita" : 22,
#     "kurt" : 65
# }

# def func():
#     while True:
#         name = input("Enter your name : ")
#         name_lower = name.lower()

#         if name_lower in student_grade:
#             grade = student_grade[name_lower]

#             if grade >= 75:
#                 print(f"Hi {name_lower.capitalize()}!, You Distinction grade is {grade}")

#             elif grade >= 60:
#                 print(f"Hi {name_lower.capitalize()}!, You First Divison grade is {grade}")                

#             elif grade >= 45:
#                 print(f"Hi {name_lower.capitalize()}!, You Distinction grade is {grade}")    

#             else:
#                 print(f"Hi {name_lower.capitalize()}!, Mom's flying chapal received at {grade}km/hr")            

#             choice = input("Enter 0 to exit, 1 to continue : ")
#             if choice == '0':
#                 break
#             elif choice == '1':
#                 continue
#             else:
#                 print("Invalid Choice")
#                 break
#         else:
#             print("Invalid Name")   


# func()