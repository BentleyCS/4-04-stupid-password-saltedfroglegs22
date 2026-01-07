"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    pass
    password = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = alphabet[:l]

    for c1 in range(1, n+1):
        for c2 in range(1, n + 1):
            for c3 in letter:
                for c4 in letter:
                    for c5 in range(1, n+1):
                        if c5 > c1 and c5 > c2:
                            password.append(str(c1)+str(c2)+str(c3)+str(c4)+str(c5))

    return password



