"""Its time for yet another challenge, and this time it has been prepared by none other than Monk himself for Super-Hardworking Programmers like you. So, this is how it goes:

Given N points located on the co-ordinate plane, where the  point is located at co-ordinate , , you need to answer q queries.

In the  query, you shall be given an integer , and considering you draw a circle centered at the origin  with radius , you need to report the number of points lying inside or on the circumference of this circle.

For each query, you need to print the answer on a new line.

Input Format :

The first line contains a single integer N denoting the number of points lying on the co-ordinate plane. Each of the next N lines contains 2 space separated integers  and , denoting the x and y co-ordintaes of the  point.

The next line contains a single integer q, denoting the number of queries. Each of the next q lines contains a single integer, where the integer on the  line denotes the parameters of the  query .

Output Format :

For each query, print the answer on a new line.

Constraints :





SAMPLE INPUT
5
1 1
2 2
3 3
-1 -1
4 4
2
3
32
SAMPLE OUTPUT
3
5
Explanation
For the  query in the sample, the circle with radius equal to 3 looks like this on the co-ordinate plane

enter image description here

The points : ,  and  lie inside or on the circumference of the circle."""
import math


def countPoints(data, r,i):
    """

    :type data: object
    """
    area = math.pi * r * r;
    count = 0
    for x in data:
        r1 = math.sqrt(math.pow(int(x[0]), 2) + math.pow(int(x[1]), 2))
        a = math.pi * r1 * r1
        if area >= a:
            count += 1
    print count


if __name__ == '__main__':
    no = int(raw_input())
    data = []
    radius = []
    for i in range(no):
        data1 = raw_input()
        data1 = data1.split(" ")
        data.append([data1[0], data1[1]])
    testCase = input()

    for i in range(testCase):
        a = int(raw_input())
        radius.append(a)
    for i in range(testCase):
        countPoints(data, int(radius[i]),i)
