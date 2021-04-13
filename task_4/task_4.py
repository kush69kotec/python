# добавил файл piton.py для проверки скрипта
import os
from pathlib import Path

folder = Path.cwd()
files_dict = {}
for file in os.scandir(folder):
    if os.path.isfile(file):
        file_size = os.path.getsize(file)
        threshold = 10 ** len(str(file_size))
        try:
            files_dict[threshold] += 1
        except KeyError:
            files_dict[threshold] = 1
