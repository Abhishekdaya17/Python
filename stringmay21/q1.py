'''1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc'''
n=input("input:")
unique=""
for i in range(0,len(n)):
    ch=n[i]
    if ch not in unique:
        unique=unique+ch
print(unique)