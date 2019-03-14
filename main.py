import pandas
print("Parth Roy")
#If condition true then print 1

if 11==10:
    print 1
else:
    print 0
"""
multi line comment
"""

print "Parth Roy", "Royal Dreams"# comma will give the space
print("c:\\narayan")#C drive file print
print("c:\"narayan")
print("Parth\tRoy")#print end="" ending string given

a=10
b=20
print a+b
print type(a)
a="10"
b="20"
print int(a)+int(b)


print 5*"Parth Roy\n"
print 10*str(int(a)+int(b))

# num=input()
mystr="Parth Roy is Good Boy"
print(len(mystr))
print(mystr[0:])
print(mystr[0:19:200])
print(mystr[-10:])
print(mystr[-5:-2])

print(mystr.find("o"))
print mystr.lower()
print mystr.upper()
print mystr.capitalize()
print mystr.endswith("Boy")
print mystr.replace("Good", "Clever")