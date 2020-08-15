#Dictionary
dict = {
    "Anshul": "Python",
    "Harshit": "C++",
    "Aryan": "CSS",
    "Bhawna": {"B": "Bread",
               "L": "Roti",
               "D": "Chicken"
               }
}
print(type(dict))
print(dict)
dict["Jinna"] = "HTML"
print(dict)
print(dict["Anshul"])
print(dict["Bhawna"]["D"])
print(dict["Jinna"])
#
del dict["Bhawna"]
print(dict)
#
dCopy = dict.copy()
dCopy["Aryan"] = "Java"
print(dCopy)
print(dict)
dCopy.update({"Leena":"JS"})
print(dCopy)
print(dCopy.keys())
print(dCopy.values())
print(dCopy.items())

