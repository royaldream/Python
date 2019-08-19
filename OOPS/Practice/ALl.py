def a():
    raw = raw_input()
    raw = raw.split(" ")
    no = int(raw[0])
    find = int(raw[1])
    data = raw_input().split(" ")
    data = [int(a) for a in data]
    index = -1
    for a in range(len(data)):
        if data[a] == find:
            index = a + 1
    print index


# data = None
import math


def binarySearch(data, low, high, key):
    low, high, key = int(low), int(high), int(key)
    # print low, high, key
    while low <= high:
        mid = math.ceil((low + high) / 2)
        mid=int(mid)
        # print data[int(mid)]
        if data[mid] < key:
            low = mid + 1
            # print "l", low
        elif data[mid] > key:
            high = mid - 1
            # print "h", high
        else:
            return mid+1
    return -1


def b():
    no = int(raw_input())
    data = raw_input()
    data = data.split(" ")
    data = [int(a) for a in data]
    data.sort()
    testCase = int(raw_input())
    tData = []
    for i in range(testCase):
        tData.append(int(raw_input()))
    # print data, tData
    outData = [binarySearch(data, 0, len(data), x) for x in tData]
    for a in outData:
        print str(a)


if __name__ == '__main__':
    b()
