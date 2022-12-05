from sys import stdin

max = 0
max2 = 0
max3 = 0
curr = 0
for line in stdin:
    if line == "\n":
        if curr > max:
            max3 = max2
            max2 = max
            max = curr
        elif curr > max2:
            max3 = max2
            max2 = curr
        elif curr > max3:
            max3 = curr
        curr = 0
    else:
        curr = curr + int(line)
print(max + max2 + max3)