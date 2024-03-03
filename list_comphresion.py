names = ['ram', 'shyam', 'hari', 'ryhtm', 'rj']
v = 'aeiou'
# vowel_names = []
# for name in names:
#     for char in name:
#         if char.lower() in v and name not in vowel_names:
#             vowel_names.append(name)
# print(vowel_names)


vowel_names = [name for name in names if 'a' in name.lower() or 'e' in name.lower() or 'i' in name.lower() or 'o' in name.lower() or 'u' in name.lower()]

v_names = [name for name in names if any(char.lower() in v for char in name)]

print(v_names)
print(vowel_names)



# names = ['ram', 'shyam', 'hari', 'ryhtm', 'rj']

# vowels = {'a', 'e', 'i', 'o', 'u'}

# name_with_vowel = [item for item in names if vowels.intersection(item)]

# print(name_with_vowel)


# num = list(range(2, 50))

# result = [n for n in num if n % 3 == 0 and n % 2 == 0]

# print(result)


#func that takes price in the format '$60000' and retur int price

# def print_price(p):
#     int_price = int(p[1:])
#     return int_price

# def clean_price(p):
#     return int(p.replace('$', ''))

# a = lambda p: int(p.replace('$', ''))
# print(a('$600000'))

# price = (input("Enter price : "))


# print(print_price(price))
# print(clean_price(price))


#func that returns domain of email address

# domain = lambda email: email.split('@')[-1]

# print(domain('exmple@edu.np'))

# lambda func that takes a string and check the first vowel in the string

#LAMBDA FUNC THAT TAKES STRING AND RETURNS THE length of string
#lambda func that takes string and returns last char

# lenght = lambda s: len(s)
# print(lenght("Nirvana"))

# last_c = lambda s: s[-1]
# print(last_c("Nirvana"))