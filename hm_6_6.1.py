import sys
if len(sys.argv) <= 1:
    print('Number is required')
    sys.exit(-1)
with open('bakery.csv', 'a', encoding="utf-8") as f:
    f.write(sys.argv[1] + '\n')

