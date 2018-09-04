'''
split() command can 


'''
#!/usr/bin/env python
import sys
data = sys.stdin.read()
cut_word = []
for line in data.split("\n"):
    start =4
    end = 8
    if line and len(line.split()) > start:
        cut_word.append(line.split()[start:end])
[print(i) for i in cut_word]
