import re
handle = open("regex_sum_2349653.txt")

lst = list()
for line in handle:
    line = line.rstrip()
    tmp = re.findall('([0-9]+)', line)
    lst.extend(tmp)
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(sum(lst))
