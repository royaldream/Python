def gcdNo(no1, no2):
    global gcd
    i = 1
    while i <= no2 and i <= no1:
        if no2 % i == 0 and no1 % i == 0:
            gcd = i
        i += 1
    return gcd


def main():
    print "Enter Two Number : "
    no1 = int(input())
    no2 = int(input())
    print gcdNo(no1, no2)


if __name__ == "__main__":
    main()
