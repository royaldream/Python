"""Monk and his friend Micro are on a quest to find the answer of Life, Universe and Everything. In order to complete
it they need to answer Q queries on an array A having N integers. The queries can be of following two types: Find the
number of numbers in A which are not less than x. Find the number of numbers in A which are greater than x. Help them
complete the quest and be back in time for the next Code Monk Challenge.

Input Format:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.
Third line consists of a single integer denoting Q.
Each of the following Q lines consists of a query of one of the given two types.

Output Format:
For each query print the required answer in new line.

SAMPLE INPUT
4
1 2 3 4
3
0 5
1 3
0 3
SAMPLE OUTPUT
0
1
2
Explanation
For first query, there are no numbers in the array which are not less than 5 so answer for first query is 0.
For second query, 4 is the only number greater than 3, so answer is 1.
For third query, 3 and 4 are the numbers in array which are not less than 3, so answer is 2."""


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


import math as Math

if __name__ == '__main__':
    two_no = raw_input()
    two_no = two_no.split()
    no = int(two_no[0])
    sum = int(two_no[1])
    print no, sum
    testCase = int(raw_input())
    data = []
    for i in range(testCase):
        d1 = raw_input()
        d1 = d1.split(" ")
        data.append([d1[0], d1[1]])
    root = Node(no)
    totalNode = Math.pow(2, no) - 1
    a = no
    root.insert(2)
    root.insert(3)
    root.insert(2)
    root.insert(4)
    root.insert(4)
    root.insert(5)
    # for i in range(int(totalNode) / 2):
    #     a -= 1
    #     root.insert(no)
    #     a += 1
    #     root.insert(a)
    #     a -= 1
    root.PrintTree()
