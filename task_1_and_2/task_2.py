import os
from pathlib import Path


# не было времени разобраться как именно должен обрабатываться шаблон YAML, но мне подсказали как должен выглядеть
# шаблон и я отформатировал файл вручную для этого соответствия - немного сжульничал, и так легче парсить оказалось.
# В общем суть в том, что я отталкиваюсь от количества пробелов в файле, чтобы контролировать внутренний уровень файла.


def file_name(string):
    new_name = string.replace('|', '').replace(' ', '').replace('-', '').replace(':', '').strip()
    return new_name


with open('config.yaml', 'r', encoding='utf-8') as f:
    dir_path = Path.cwd()
    inside_lvl = 0
    for line in f:
        name = file_name(line)
        new_inside_lvl = int((line.count(' ') - 1) / 4)
        if line.endswith(':\n'):
            if new_inside_lvl > inside_lvl:
                dir_path = dir_path.joinpath(name)
                inside_lvl += 1
            elif inside_lvl == 0:
                dir_path = dir_path.joinpath(name)
            elif new_inside_lvl == inside_lvl:
                dir_path = Path(dir_path).parents[0].joinpath(name)
            elif new_inside_lvl < inside_lvl:
                dir_path = Path(dir_path).parents[inside_lvl - new_inside_lvl].joinpath(name)
                inside_lvl = new_inside_lvl
            os.mkdir(dir_path)
        else:
            file = dir_path.joinpath(name)
            if not os.path.exists(file):
                open(file, 'w', encoding='utf-8').close()
