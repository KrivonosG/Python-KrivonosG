import os, math, json, sys

def search():
    for root, _, files in os.walk('some_data'):
        for file in files:
            yield os.path.join(root, file)


result = {}
for f in search():
    key = os.stat(f).st_size
    _, ext = os.path.splitext(f)
    if key:
     key = 10 ** math.ceil(math.log(key, 10))
    result.setdefault(key, (0, set()))
    a, b = result[key]
    b.add(ext)
    result[key] = (a + 1, b)

for k, v in result.items():
    a, b = result[k]
    result[k] = (a, list(b))

print(json.dump(result, sys.stdout))
