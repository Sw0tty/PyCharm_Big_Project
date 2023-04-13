import math
import os


def dir_info():
    address_list = []
    dirs_list = []
    files_list = []
    for address, dirs, files in os.walk(os.getcwd()):
        if '.git' in address:
            continue
        address_list.append(address)
        dirs_list.append(dirs)
        files_list.append(files)
    return address_list, dirs_list, dirs_list


def to_dict(lst):
    dict_ = {}
    for i in lst:
        dict_.update([(i, i)])
    return dict_


my_dict = {"first_one": "we can do it"}
def biggest_dict(**kwargs):
    return my_dict.update(kwargs)


if __name__ == '__main__':
    print(dir_info())
    print(to_dict(['grey', (2, 17), 3.11, -4]))
    biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
    print(my_dict)
    print(math.log2(20))
