names = ["Kurt", "Laney", "Chris", "Eddie"]

#heterogenous in nature
#list is mutable
#list is numbered | indexed
a =[1, 1.1,False, "Kurt"]
print(a[0])
for x in a:
    print(x)

print(len(a))
print("KURT".lower() in names)   #false

names.append("Jimmy")
print(names)

names.insert(1, "Axle")
print(names)

names.insert(3, "Chester")
print(names)

names.remove("Chester")
print(names)

# Updating Values |Replacing
names[1] = "Eminem"
print(names)

#Extend 
bands = ["Nirvna", "Alice In Chains", "Pearl Jam", "Audioslave"] 

print(names + bands)
print(names)

names.extend(bands)
print(names)
print(bands)

