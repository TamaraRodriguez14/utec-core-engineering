#!/usr/bin/env python3
alphabet = ""
for code in range(ord('a'), ord('z') + 1):
    if chr(code) != 'q' and chr(code) != 'e':
        alphabet += chr(code)
print(alphabet)
