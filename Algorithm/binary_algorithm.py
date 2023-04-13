def binary_algorithm(list_, search_item):
    count = 1  # Счетчит попыток
    high = len(list_) - 1  # последний номер элемента списка
    low = 0  # Первый номер элемента списка
    while low <= high:  # Ищем, пока не сведемся к одному элементу
        mid = int((low + high) / 2)  # Находим середину
        guess = list_[mid]  # Передаем середину и узнаем значение элемента в списке
        if guess == search_item:
            return "Искомый элемент '{}' найден за {} попыток." \
                   "Он находится в списке под индексом '{}'".format(search_item, count, mid)
        if guess > search_item:
            high = mid - 1  # Если искомое число меньше предпологаемого, отбрасываем все числа больше чем в середине
        else:
            low = mid + 1
        count += 1
    return "Элемента '{}' нет в списке".format(search_item), count


print(binary_algorithm([i for i in range(1, 10000)], 1))
