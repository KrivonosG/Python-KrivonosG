import os, shutil

my_project = 'my_project'
dir_name = 'templates'

dir_name = os.path.join(my_project, dir_name)


def search():
    for root, _, files in os.walk(my_project):
        for file in files:
            if file.endswith('.html'):
                yield os.path.join(root, file)

for i in search():
        to = i.replace(my_project, dir_name)
        os.makedirs(os.path.dirname(to), exist_ok = True)
        shutil.copy2(i, to)

