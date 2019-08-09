import math as M


def strongornot(no):
    ono = no
    flag = False
    sum, fsum, i = 0, 0, 0
    while no > 0:
        n = no % 10
        no = no / 10
        # sum += n
        fsum += M.factorial(n)

    if fsum == ono:
        flag = True
    else:
        flag = False
    print ono, fsum
    return flag


def main():
    no = long(input())
    print strongornot(no)


if __name__ == '__main__':
    main()
