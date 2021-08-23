
def parse(l):
    l = l.split(" ")
    addr = l[0]
    return addr


addresses = []
with open('nginx_logs.txt') as f:
    for k in f.readlines():
        addresses.append(parse(k.strip()))

m = 0
addr = ""
spam = {}

for a in addresses:
    spam.setdefault(a, 0)
    spam[a] += 1

for k in spam:
    if m < spam[k]:
        m = spam[k]
        addr = k
print(f'Max count: {m}, address: {addr}')

