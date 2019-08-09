"""Monk introduces the concept of palindrome saying,"A palindrome is a sequence of characters which reads the same backward or forward."
Now, since he loves things to be binary, he asks you to find whether the given string is palindrome or not. If a given string is palindrome, you need to state that it is even palindrome (palindrome with even length) or odd palindrome (palindrome with odd length).

Input:
The first line consists of T, denoting the number of test cases.
Next follow T lines, each line consisting of a string of lowercase English alphabets.

Output:
For each string , you need to find whether it is palindrome or not.
If it is not a palindrome, print NO.
If it is a palindrome, print YES followed by a space; then print EVEN it is an even palindrome else print ODD.
Output for each string should be in a separate line.
See the sample output for clarification."""


def palindrome(data):
    flag = True
    for i in range(0, len(data) / 2):

        if data[i] != data[len(data) - i - 1]:
            # print data[i],data[len(data)-i-1],
            flag = False
    if len(data) % 2 == 0 and flag:
        return "YES EVEN"
    elif flag:
        return "YES ODD"
    else:
        return "NO"


if __name__ == "__main__":
    n = int(input())
    for a in range(n):
        d = raw_input()
        # d = d.split()
        print palindrome(d)
