list = [
    "C", "C++", "Python", "Java", "JavaScript", "R", "Ruby"
]

for items in list:
    print(items+" and", end=" ")
print("other languages.")

# join function

a =  " and ".join(list)
print("\n"+a)
a =  " , ".join(list)
print("\n"+a)
a =  " or ".join(list)
print("\n"+a)
