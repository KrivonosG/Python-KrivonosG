# email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
import re
address = 'someone@geekbrainsru'


def email_parse(address):
    parsed = re.findall(r'(^\w+)@((\w+)\.(\w{2,}))$', address)
    if not parsed:
        raise ValueError(f'wrong email: {address}')
    return dict(zip(['username', 'domain'], parsed[0]))

try:
 print(email_parse(address))
except ValueError:
    print(f'address {address} is not correct e-mail address')