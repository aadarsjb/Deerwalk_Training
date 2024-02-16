a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# non primitive data types
# list set tuple dictionary

# why list
# stores multiple values

# a = []  # preferred
# b = list()

# print(type(a))
# print(type(b))


# names = ['ram', 'shyam', 'hari']
# print(names)

# properties 
#heterogenous
# a = [1, 1.1, True, False, 'ramesh']
# print(a)


# mutable/changeable
# add/remove/update

# indexed/ordered
a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# print(a[0])
# print(a[-1])
# print(a[10])
# print(a[::2])

a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# print(len(a))
# print('shyam' in a)
# print('Shyam' in a)
# print('SHYam'.lower() in a)

a = ['ram', 'shyam', 'hari']
# add
# append, insert
# a.append('rita')
# a.append('sita')
# print(a)

# a.insert(1, 'rita')
# a.insert(3, 'sita')
# a.insert(0, 'rita')
# print(a)


# delete
a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# remove, pop, del
# a.remove('ram')
# a.remove('rita')
# a.remove('sita')
# a.remove('ramesh')

# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()


a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# a.pop(2)
# print(a)

# del a[0]
# print(a)


# update values
# a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# a[0] = 'ramesh'
# print(a)

# a = ['ram', 'ram', 'ramesh', 'hari']
# print(a)



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# print(thislist + tropical)
# print(thislist)


a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# a.clear()
# print(a)


# a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# a.sort()
# print(a)

# a = [1,8,3,0,4,2]
# a.sort()
# print(a)


# a = [1, 'umesh', 10.1, 'ram']
# a.sort()
# print(a)



# a = [True, 1, False, 10]
# a.sort()
# print(a)

a = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# a.reverse()
# print(a)

# a.sort()
# a.reverse()
# a.sort(reverse=True)
# print(a)




# append() --> add to the last
# insert() --> adds to the specified index


# remove() --> removes the given value
# pop() --> removes the given index. if no index is given removes the last index

# del --> removes the given index

# a = ['ram', 'ram', 'hari', 'ram', 'sita', 'gita']
# print(a.count('ram'))
# print(a.index('ram'))


# a = ['ram', 'ram', 'hari']
# b = a
# b[0] = 'ramesh'
# print(b)
# print(a)


a = ['ram', 'shyam', 'hari']
b = a.copy()
b[0] = 'umesh'
print(b)
print(a)


