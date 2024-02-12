#!/usr/bin/env python3.7
# Indexing and Slicing Python Strings

m = input("Enter a text : ")
print("Length : ", len(m))
print ("First character : ", m[0])
print("Last character : ", m[-1])
print("Middle character : ", m[int(len(m)/2)])
print("Even index characters : ", m[0::2])
print("Odd index characters : ", m[1::2])
print("Reversed text : ", m[::-1])



