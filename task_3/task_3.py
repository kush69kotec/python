import os
from shutil import copyfile
root_dir = '/home/pcfourtwenty/PycharmProjects/python_basics/homework_7/task_3'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            dir_path = os.path.join('templates', os.path.basename(root))
            print(os.path.basename(root), root)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            copyfile(os.path.join(root, file), os.path.join(dir_path, file))





