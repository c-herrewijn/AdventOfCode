found = False
count = 0
with open("06/input.txt") as file:
    s = file.read()
    sub = s[count:count+4]
    while not found:
        sub = s[count:count+4]
        found = (len(set(sub)) == len(sub))
        count+=1

# result
print(count+3)
