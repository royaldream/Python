def isLeapYear(data):
    year = int(data)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not Leap Year"


def main():
    print "Enter Year : "
    year = int(input())
    print isLeapYear(year)


if __name__ == "__main__":
    main()
