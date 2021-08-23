import sys
from itertools import zip_longest

with open("users_hobby.txt", "w", encoding="utf-8") as result:
    with open('users.csv', encoding="utf-8") as users:
        with open('hobby.csv', encoding="utf-8") as hobbies:

            len_users = sum(1 for _ in users)
            len_hobbies = sum(1 for _ in hobbies)

            if len_hobbies > len_users:
                sys.exit(1)

            users.seek(0)
            hobbies.seek(0)
            for user, hobby in zip_longest(users, hobbies):
                result.write(f'{user.strip()}: '
                             f'{hobby.strip() if hobby is not None else hobby}\n')