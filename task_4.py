import os, math

def search():
    for root, _, files in os.walk('some_data'):
        for file in files:
            yield os.path.join(root, file)


result = {}
for f in search():
    key = os.stat(f).st_size
    if key:
     key = 10 ** math.ceil(math.log(key, 10))
    result.setdefault(key, 0)
    result[key] += 1

for k, v in sorted(result.items()):
    print("for size ", k, " files ", v)
#  размер файла можно получить из атрибута .st_size объекта os.stat