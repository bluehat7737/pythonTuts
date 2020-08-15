# # for loop
#
# list = [
#     ["Anshul", 2],
#     ["Bhawna", 50],
#     ["Aryan", 3],
#     ["Harshit", 6]
# ]
#
# dict = dict(list)
#
# for name, lolly in dict.items():
#     print(name, "and lolly is",lolly)

list = [2, 5, 8, 5, 64, 64, "Anshul", "Harshit"]

for items in list:
    if str(items).isnumeric() and items > 6:
        print(items)
