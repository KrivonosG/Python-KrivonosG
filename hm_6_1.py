
with open('nginx_logs.txt') as f:
    for k in f.readlines():
        def parse(l):
            l = l.split(" ")
            addr = l[0]
            request = l[5]
            url = l[6]
            return addr, request[1:], url
        print(parse(k.strip()))

