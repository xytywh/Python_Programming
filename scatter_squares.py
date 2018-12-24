import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values, c='red', edgecolors='None', s=40)
# plt.scatter(x_values, y_values, c=[0, 0, 0.8], edgecolors='None', s=40)
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, edgecolors='None', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox='tight')
