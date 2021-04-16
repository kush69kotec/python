import re


# в этом задании я довольно сильно упростил задачу, из-за того что не успевал по времени, но основное
# условие выполняется


def email_parse(string):
    try:
        email_dict = {}
        EMAIL = re.findall(r'(\w+)@(\w+[.]\w+)', string)
        email_dict[EMAIL[0][0]] = EMAIL[0][1]
        return email_dict
    except IndexError:
        print(f'wrong email: {string}')
        raise ValueError(f'wrong email: {string}')


task_dict = email_parse('kush69kotec@gmail.com')
print(task_dict)
