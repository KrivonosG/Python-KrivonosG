import sys
from itertools import zip_longest

if len(sys.argv) < 4:
    print(f'Usage: {sys.argv[0]} <users file name> <hobby file name> <result file name>')
    sys.exit(1)

users_file_name = sys.argv[1]
hobby_file_name = sys.argv[2]
result_file_name = sys.argv[3]
with open(result_file_name, "w", encoding="utf-8") as result:
    with open(users_file_name, encoding="utf-8") as users:
        with open(hobby_file_name, encoding="utf-8") as hobbies:

            len_users = sum(1 for _ in users)
            len_hobbies = sum(1 for _ in hobbies)

            if len_hobbies > len_users:
                sys.exit(1)

            users.seek(0)
            hobbies.seek(0)
            for user, hobby in zip_longest(users, hobbies):
                result.write(f'{user.strip()}: '
                             f'{hobby.strip() if hobby is not None else hobby}\n')
