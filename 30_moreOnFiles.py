f = open("test.txt")

print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(29)
print(f.tell())
print(f.readline())

# not working
print(f.readline())
f.close()   

