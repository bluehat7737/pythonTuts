import math
# 1
me = "Anshul"
str = "Thia is %s" % me
print(str)

# 2
s1 = 1
s2 = "this is a string"
s3 = "using tuple : %s %s" % (s1, s2)
print(s3)

# 3
a = 3
b = "This is {1} {0}"
c = b.format(a, me)
print(c)

# 4 f-string
str1 = "string 1"
str2 = "string 2"
fstr = f"this is {str1} {str2} {7*5} {math.sin(90)}"
print(fstr)
