import matplotlib.pyplot as plt
import numpy as np

# fruits = ["20", "30", "40", "50"]
# counts = [74.18, 105.43, 96, 187]
# plt.bar(fruits, counts)
# plt.title("ГА, количество популяций - 35, селекция - 40%, предметов - 25")
# plt.xlabel("Шанс мутации, %")
# plt.ylabel("Время, с")
# plt.show()

# fruits = ["10", "30", "50", "70"]
# counts = [91.26, 61.43, 77.65, 120.54]
# plt.bar(fruits, counts)
# plt.title("ИИС, количество популяций - 55, селекция - 40%, предметов - 45")
# plt.xlabel("Количество клонов, шт")
# plt.ylabel("Время, с")
# plt.show()

# # line 1 points
# x1 = [0, 25, 35, 45, 55]
# y1 = [0, 26.12, 79.66, 181.91, 474.12]
# # plotting the line 1 points
# plt.plot(x1, y1, label="ГА")
# # line 2 points
# x2 = [0, 25, 35, 45, 55]
# y2 = [0, 7.12, 25.95, 121.76, 289.21]
# # plotting the line 2 points
# plt.plot(x2, y2, label="ИИС")
# plt.xlabel('Количество предметов, шт')
# # Set the y axis label of the current axis.
# plt.ylabel('Время работы, с')
# # Set a title of the current axes.
# plt.title('Сравнение скорости ГА и ИИС')
# # show a legend on the plot
# plt.legend()
# # Display a figure.
# plt.show()

index = np.arange(4)
values1 = [12, 42.68, 37.32, 8]
values2 = [8.91, 34.51, 44.91, 11.67]
bw = 0.3
algs = ['ГА', 'ИИС']
plt.axis([-0.5, 4, 0, 50])
plt.title('Сравнение качества ГА и ИИС (1000 итераций)', fontsize=16)
plt.bar(index, values1, bw, color='y')
plt.bar(index + bw, values2, bw, color='b')
plt.xticks(index + 0.5 * bw, [0, 1, 2, 3])
plt.xlabel('Количество уменьшенных контейнеров, шт')
plt.ylabel('Процент случаев, %')
plt.legend(algs, loc=2)
plt.show()
