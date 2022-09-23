""""
itertools.combinations(iterable, r)
This tool returns the "r" length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
Sample code:
>>> from itertools import combinations
>>> 
>>> print(list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]


Task

You are given a string S.
Your task is to print all possible combinations, up to sizek, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints

0 < k <= len(S)

The string contains only UPPERCASE characters.

Output Format:

Print the different combinations of string S on separate lines.

Sample input:
HACK 2


Sample output:
A
C
H
K
AC
AH
AK
CH
CK
HK

"""

from itertools import combinations

alfabet = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, 
"L":12, "M":13, "N":14, "O": 15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, 
"W":23, "X":24, "Y":25, "Z":26}

S = "HACK"
k = 2
lista = list(combinations(S, k))
#print(lista)

# iterar cada letra no alfabeto e retornar o número correspondente a sua posicao no alfabeto
S_order = []
for i in S:
    for k,v in alfabet.items():
        if i == k:
            S_order.append(v)

#necessairy print (S_order): [8, 1, 3, 11]
print(S_order)

#now sorted (S_order): [1,3,8,11]
S_order.sort()
print(S_order)