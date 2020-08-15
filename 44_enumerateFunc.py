ll = [
    'Anshul',
    'Arysn',
    'Harshit',
    'Bhawna'
]

# 1
i=1
for items in ll:
    if i%2 is not 0:
        print(items)
    i += 1

# 2
for index, items in enumerate(ll):
    if index%2==0:
        print(items)

