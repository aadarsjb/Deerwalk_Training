#filter() ----> filter the values / narrow down
# output length may be smaller or same length as input
#function returns either True or False


# def is_even(x):
#     return True if x % 2 == 0 else False

# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(filter(is_even, num)))
# # func inside filter() should always return boolean value


# print(list(filter(lambda x: True if x% 2 == 0 else False, num)))

#map() ----> transform values
# refrence functions convert values 
# input length = output length
# func has expression to convert the values to another values

# def square_it(n):
#     return n ** 2

# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(map(square_it, num)))

# print(list(map(lambda x: x ** 2, num)))

# sq_values = [ x ** 2 for x in num]
# print(sq_values)

#--------------------------------------------------------------------------------------------

#select even numbers that are multiple of 3
num = range(2, 50)
even_num = [ x for x in num if x % 2 == 0 and x % 3 == 0]
print(even_num)

print(list(filter(lambda x: x % 2 == 0 and x % 3 == 0, num)))

#------------------------------------------------------------------------------------------------

#change name into uppercase
names = ['ram' , 'shyam', 'hari', 'rita']
upper_name = [name.upper() for name in names]
print(upper_name)

print(list(map(lambda upper_name: upper_name.upper(), names)))

#----------------------------------------------------------------------------------------------------

#print name that starts with 'r' or 'R'
given_name = ['ram' , 'shyam', 'hari', 'rita', 'Ramesh', 'Riya']
name_r = [name for name in given_name if name.startswith('r') or name.startswith('R')]
print(name_r)

print(list(filter(lambda x: x.startswith('r') or x.startswith('R'), given_name)))

#----------------------------------------------------------------------------------------------------------
#select all the names that has r or R in it.
n = ['ram' , 'shyam', 'sonu', 'rita', 'Ramesh', 'priya', 'supriya']

n_r = [name for name in n if 'r' in name.lower()]
print(n_r)

print(list(filter(lambda i: 'r' in i.lower(), n)))

#-------------------------------------------------------------------------------------------

#take the square root of all values
num_1 = [1, 4, 9, 16, 25]

sqrt_value = [x ** 0.5 for x in num_1]
print(sqrt_value)  

print(list(map(lambda x: x ** 0.5, num_1)))

#--------------------------------------------------------------------------------------------