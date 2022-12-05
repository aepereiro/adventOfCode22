from sys import stdin

max = 0
curr = 0
for line in stdin:
    if line == "\n":
        if curr > max:
            max = curr
        curr = 0
    else:
        curr = curr + int(line)
print(max)