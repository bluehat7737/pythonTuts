# f = open("0/1.txt", "a")
# n = f.write("\nMy name is Anshul")
# print(n)
# f.close()


f = open("0/file.txt", "r+")

print(f.read())
f.write("OK")
print(f.read())
f.close()