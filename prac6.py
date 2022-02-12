"""VISHWA PATEL - 20CE110
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. """
#importing counter file from collections
from collections import Counter
l=[]
#checking the condition
for i in range(int(input())):
    l.append(input())

c=Counter(l)
print(len(c))
for i in c:
    print(c.get(i),end=' ')

