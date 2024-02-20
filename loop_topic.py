# code reusability

# while condition:
#     statment

# i = 0
# while i < 5:
#     print("Damnnnn")
#     i += 1

#infinnite loop
# i = 0
# while i < 5:
#     print("Damnnnn")
    #-------------------------#
# i = 0
# while i < 5:
#     print("Damnnnn")
#     i -= 1


#for loop

# for variable_name in iterables(str, list, set, tuples, dict, range)
    
#print(list(range(2, 10)))

# name = 'Kurt'
# for item in name:
#     print(item)

# bands = ["Nir", "AIC", "PJ", "AS"]

# for name in bands:
#     print(name)

# i = 0
# while i < 4:
#     print(bands[i])
#     i += 1

# koops in dict

#---------- EXERISE ----------------
#given list names = ['ram', 'shyam', 'hari', 'sita']
# print names using for and while loop
#no matter what the string length is

#student_grade = {'shyam': 32, 'hari': 18, 'ram': 25}
#print all the names and corresponding grade
#Hi Shyam, Your grade is 32

#print even numbers from 2 to 30 including 30

#crete a list from 2 to 50
#separate odd and even number from the list into separate list
# even_list
#odd_list

#use break continue to run the program without stopping
# enter 0 to exit 1 to continue


#break and continue

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if item == 4:
        break
    else:
        print(item)
        print("***")


#continue stops current iteration and passes to next iteration

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in l:
    if item % 2 == 0:
        continue
    else:
        print(item)
