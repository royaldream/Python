# set is unique data store
list = [10, 20, 30]
s = set(list)
print type(list)
print type(s)
s.add(1)
s.add(2)
s.add(1)
print s
s1 = s.union({10, 20, 30})
s2 = s.intersection({10, 20, 30})
print s1, s2