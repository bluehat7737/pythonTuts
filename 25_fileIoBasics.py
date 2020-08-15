# File IO Basics

"""
'r' - read
'w' - write
'x' - create file if not exist
'a' - add more content
't' - text mode
'b' - binary mode
'+' - read & write
"""

f = open("0/file.txt")

print(f.readlines())

# content = f.read()
# print(content)

# for line in f:
#     print(line, end="")

f.close()