import re
# почему то такое сумасшедшее выражение по поиску работает куда быстрее, чем почти завершённые короткие сочетания)
with open('task_2/nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        PARSED_LINE = re.findall(
            r'(\d+.+\d)\s-\s-\s\S([\s\d+:/\w]+)\S\s\S(\w+)\s(\S\w+\S\w+)\s\w+\S\d+\S\d+\S\s(\d+)\s(\d+)', line.strip())
        print(PARSED_LINE)
