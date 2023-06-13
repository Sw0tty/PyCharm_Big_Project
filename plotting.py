import matplotlib.pyplot as plt


# ------График------------
# x_cords = [0, 1, 2, 3, 4]
# y_cords = [0, 3, 1, 5, 2]
#
# plt.plot(x_cords, y_cords, marker='o')  # Строит график
#
# plt.title("Тестовый график")
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
#
# plt.xlim(-1, 10)
# plt.ylim(-1, 6)
#
# plt.xticks(x_cords, [i for i in range(2016, 2021)])
# plt.yticks([0, 1, 2, 3, 4, 5], [f"${i}m" for i in range(0, 6)])
#
# plt.grid(True)
# plt.show()  # Выводит результат построения
# -------------------------

# ------Гистограмма------------
# left_edges = [i for i in range(0, 41, 10)]
# height = [i for i in range(100, 501, 100)]
#
# bar_width = 10
#
# plt.bar(left_edges, height, bar_width, color=('r', 'm', 'b'))
#
# plt.title("Тестовая гистограмма")
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
#
# plt.xticks([5, 15, 25, 35, 45], [i for i in range(2016, 2021)])
# plt.yticks([i for i in range(0, 501, 100)], [f"${i}m" for i in range(0, 6)])
#
# plt.show()
# -------------------------

# ------Круговая диаграмма-----------
values = [20, 60, 80, 40]

slice_labels = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']

plt.pie(values, labels=slice_labels)
plt.title("Продажи")
plt.show()
# -------------------------
