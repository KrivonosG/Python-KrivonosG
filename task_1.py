import os

main_dir = "my_project"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp"]

if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    for dir in sub_dirs:
        os.mkdir(os.path.join(main_dir, dir))
