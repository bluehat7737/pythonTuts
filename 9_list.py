grocery = ["Vim", "Lolypop", "Detergent", "Oil", "Salt"]
# grocery = [1,2,3,4,5]
print(type(grocery))
print(grocery)
print(len(grocery))
print(max(grocery))
grocery.sort()
print(grocery)
print(grocery[::2])
grocery.append("Sugar")
grocery.insert(1, "Maggie")
grocery.remove("Vim")
grocery.pop()
print(grocery)
# list = mutable
# tuple = immutable

tp = (1,2)
print(type(tp))