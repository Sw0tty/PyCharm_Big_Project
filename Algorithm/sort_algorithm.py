def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # Присваиваем переменной значение, которое выявит функция find_smallest
        new_arr.append(arr.pop(smallest))  # При помощи pop удаляем найденный элемент и сразу добавляем в новый список
    return new_arr


print(selection_sort([-1, 12, 5, -3, 6, 2, 10]))
