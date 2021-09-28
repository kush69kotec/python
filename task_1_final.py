import hashlib
task_string = input('enter your string: ')


def substring_counter(string):
    substring = ''
    sub_len = 1
    sub_start_pos = 0
    hash_list = []
    while sub_start_pos <= len(string):
        while sub_len != len(string):
            substring = string[sub_start_pos:sub_start_pos + sub_len]
            h_sub = hashlib.sha1(substring.encode('utf-8')).hexdigest()
            if h_sub in hash_list:
                break
            else:
                hash_list.append(h_sub)
            sub_len += 1
        sub_len = 1
        sub_start_pos += 1
    return len(hash_list)


print(substring_counter(task_string))
