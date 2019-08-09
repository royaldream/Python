"""Monk likes to experiment with algorithms. His one such experiment is using modulo in sorting.He describes an array modulo sorted as:
Given an integer k, we need to sort the values in the array according to their modulo with k. That is, if there are two integers a and b, and , then a would come before b in the sorted array. If  , then the integer which comes first in the given array remains first in the sorted array.
Given an initial array, you need to print modulo sorted array.

Input:
The first line consists of two integers N and k, N being the number of elements in the array and k is the number with which we need to take the modulo.
The next line consists of N space separated integers , denoting the elements of the array A.

Output:
Print the modulo sorted array of the given array."""


def main():
    d = raw_input()
    d = d.split(" ")
    n = int(d[0])
    mod = int(d[1])
    # print n, mod
    arr = raw_input()
    arr = arr.split(" ")
    iarr = [int(a) for a in arr]
    # iarr.sort()
    c = list()
    for i in range(len(iarr)):
        c.append(iarr[i] % mod)
    # for i in range(len(c)):
    #     for j in range(len(c)):
    #         if c[i] < c[j]:
    #             a,b=iarr[i],c[i]
    #             iarr[i],c[i]=iarr[j],c[j]
    #             iarr[j],c[j]=a,b

    c_ = zip(c, iarr)
    # print c_
    c_ = sorted(c_,key=lambda c_:c_[0])
    # print c_
    for i in c_:
        print(str(i[1])),
    # for i in iarr:
    #     print(str(i)),


if __name__ == "__main__":
    main()
