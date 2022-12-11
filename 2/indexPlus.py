from sys import stdin

tot = 0
for line in stdin:
    a, b = line.strip().split(' ')
    if a == "A":
        if b == "X":
            tot = tot + 3
            
        elif b == "Y":
            tot = tot + 1
            tot = tot + 3
            
        elif b == "Z":
            tot = tot + 2
            tot = tot + 6
    elif a == "B":
        if b == "X":
            tot = tot + 1
        elif b == "Y":
            tot = tot + 2
            tot = tot + 3
        elif b == "Z":
            tot = tot + 3
            tot = tot + 6
    elif a == "C":
        if b == "X":
            tot = tot + 2
            
        elif b == "Y":
            tot = tot + 3
            tot = tot + 3
        elif b == "Z":

            tot = tot + 1
            tot = tot + 6
print(tot)