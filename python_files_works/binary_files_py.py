import os


b_files_path = os.path.join(os.getcwd(), 'binary_files')

if 'string.bin' not in os.listdir(b_files_path):
    with open(os.path.join(b_files_path, 'string.bin'), 'wb') as file_handler:
        file_handler.write(b"Welcome to LinuxHint.\nLearn Python Programming.")
else:
    print("Файл 'string.bin' содержит:")
    with open(os.path.join(b_files_path, 'string.bin'), 'rb') as file_handler:
        content = file_handler.read().decode('ascii')  # Считываем строковые значения и переводим в обычный формат
        print(content)

print()

if 'number_list.bin' not in os.listdir(b_files_path):
    with open(os.path.join(b_files_path, 'number_list.bin'), 'wb') as file_handler:
        numbers = [10, 30, 45, 60, 70, 85, 99]
        b_array = bytearray(numbers)  # Конвертируем список в массив
        file_handler.write(b_array)
else:
    print("Файл 'number_list.bin' содержит:")
    with open(os.path.join(b_files_path, 'number_list.bin'), 'rb') as file_handler:
        content = list(file_handler.read())
        print(content[3])


print('string.bin' in os.listdir(b_files_path))
