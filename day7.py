#Dictionary

a = { } #preffered way
b = dict()

print(type(a))
print(type(b))



#keys -> value dnxa list ma
#values -> values dinxa list ma
#.items() -> key ra value ko tuple ko list dinxa


#del student_grade['ram]

#.get doesnot return anything/error if key doesnot exist

#,pop removes the key 
#not used frequently -> del is more preffered

#cpoy dict
student_grade = {'shyam' : 32, 'hari' : 18, 'ram' : 25}
a = student_grade
a['ram'] = 100
print(a)
print(student_grade)


#Nested Dictionary

info = {'name' : 'ram','age' : 25, 'address': {'city': 'balaju', 'district': 'kathmandu'}}
print(info['name'])
print(info['age'])
print(info['address']['city'])


