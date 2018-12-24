import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)


# 从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    lows = []
    dates = []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y/%m/%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    print(dates)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
plt.title("Daily high temperatures - 2014\nDeath Valley,CA", fontsize=20)
plt.xlabel('', fontsize=16)
# 将日期设置成斜的，避免彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
