
def menu_show():
    print "Menu\n1 : Add\n2 : Subtract\n3 : Multiply\n4 : Divide\n0 : Exit"
    choice = int(input())
    return choice

c = menu_show()
def input_taken():
    a = int(input())
    b = int(input())
    return a, b

while c != 0:

    if c == 1:
        a, b = input_taken()
        print a+b
    elif c == 2:
        a, b = input_taken()
        print a-b
    elif c == 3:
        a, b = input_taken()
        print a*b
    elif c == 4:
        a, b = input_taken()
        print a/b
    elif c == 0:
        break
    else:
        print "Wrong Choice please try again!"
    c = menu_show()

# print 5**3
