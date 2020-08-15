s = set()
print(type(s))

s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(2)
print(s)

su = s.union({1, 2, 4})
si = s.intersection({1, 2, 4})
print(su)
print(si)

sd = {4, 6, 7}
print(s.isdisjoint(sd))

sub = {1, 2}
print(sub.issubset(s))
print(s.issuperset(sub))

s.remove(3)
print(s)
