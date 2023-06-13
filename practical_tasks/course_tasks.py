def transform_string_to_integer(s):
    s = s.lower().split()
    basic_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
                  'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'двенадцать': 12, 'сорок': 40,
                  'девяносто': 90, 'сто': 100, 'двести': 200, 'тысяча': 1000, 'миллион': 1000000}
    num_from_str = []
    for num in s:
        if num in basic_dict and len(s) == 1:
            return basic_dict[num]
        elif num in basic_dict:
            num_from_str.append(basic_dict[num])
        else:
            for i in basic_dict.keys():
                if i in num or i[:-1] in num:
                    if i + 'адцать' == num:
                        num_from_str.append(int('1' + str(basic_dict[i])))
                    elif i + 'надцать' == num or i[:-1] + 'надцать' == num:
                        num_from_str.append(int('1' + str(basic_dict[i])))
                    elif i + 'дцать' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '0'))
                    elif i + 'десят' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '0'))
                    elif i + 'ста' == num or i + 'сот' == num or i[:-1] + 'сти' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '00'))
                    elif i.lower().startswith('тысяч'):
                        num_from_str.append(int(str(basic_dict['тысяча'])))

    if not num_from_str:
        return "Неизвестное число"
    elif len(num_from_str) <= 3:
        return sum(num_from_str)
    elif 1000 in num_from_str:
        return sum(i*1000 for i in num_from_str[:num_from_str.index(1000)]) +\
            sum(i for i in num_from_str[num_from_str.index(1000) + 1:])


# ----------------
def easy_factor(factorial):
    factor_list = []
    for i in range(2, factorial + 1):
        step = 1
        count = 0
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                count += 1
        if count <= 0:
            first_i = i
            sum_ = 0
            while factorial // i != 0:
                i = pow(first_i, step)
                sum_ += factorial // i
                step += 1
            if sum_ <= 1:
                factor_list.append(f"{first_i}")
            else:
                factor_list.append(f"{first_i}^{sum_}")
    return " * ".join(factor_list)


print(easy_factor(12))
# ----------------


# ----------------
def replace_duplicates(s):
    while len(set(s)) != len(s):
        for i in range(0, len(s)):
            if s.count(s[i]) != 1:
                if s[i] == 'z':
                    s = s.replace(s[i], 'a', 2)
                    s = s.replace('a', '', 1)
                else:
                    s = s.replace(s[i], chr(ord(s[i]) + 1), 2)
                    s = s.replace(chr(ord(s[i])), '', 1)
                break
    return s


print(replace_duplicates('zzzab'))
# ----------------


# ----------------
def pure_intersection(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))


arr1 = []
arr2 = [1, 2, 15, 3, 3]
print(pure_intersection(arr1, arr2))
# ----------------


# ----------------
def find_median(arr):
    if not arr:
        return None
    arr = list(sorted(arr))
    center = len(arr) - (len(arr) // 2) - 1
    if len(arr) % 2 != 0:
        return arr[center]
    else:
        return float(str(arr[center]) + '.' + str(arr[center + 1]))


print(find_median([]))
