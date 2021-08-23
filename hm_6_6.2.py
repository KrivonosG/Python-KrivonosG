import sys


def print_list(l):
    for k in l:
        print(k)


lines = []
with open('bakery.csv', encoding="utf-8") as f:
    for line in f.readlines():
        lines.append(line.strip())
if len(sys.argv) < 2:
    print_list(lines)
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
    print_list(lines[n:])
elif len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print_list(lines[n:m])
else:
    print('Wrong number of arguments')
    sys.exit(-1)
