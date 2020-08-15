with open("test.txt") as f:
    print(f.readlines())

f = open("test.txt")

print(f.tell())
print(f.readline())
f.close()