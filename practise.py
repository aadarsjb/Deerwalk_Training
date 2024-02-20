car = {
    #key : value
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(car)
print(car["brand"])
 
car2 = {   
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "electric" : False,
    "colors" : ["red", "white", "blue"]
}

print(car2)

print(len(car2))

x = car2.keys()

print(x)

car2["colors"] = "white"

print(car2)

print(car2.values())

car2["year"] = 2020
print(car2)

a = car2.items()

print(a)

print("model" in car2)

car2["available"] = "Yes"

print(car2)

car2.popitem()
print(car2)

car2.pop("model")
print(car2)


del car2["colors"]
# del car2 -> deletes the dict

#clear method empties the dict
car2.clear()
print(car2)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


