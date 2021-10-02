
import matplotlib.pyplot as plt
import numpy as np
""" 
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 自定义标签
sizes = [15, 30, 45, 10]  # 每个标签占多大
explode = (0, 0.1, 0, 0)  # 将某部分爆炸出来

plt.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=False, startangle=90)
#autopct，圆里面的文本格式，%1.1f%%表示小数有1位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
plt.axis('equal')   # 设置x，y轴刻度一致，这样饼图才能是圆的
plt.show() """
""" 


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(10*np.random.rand(100), 10*np.random.rand(100), 'o')
ax.set_title('Simple Scatter')

plt.show()
"""

N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)
plt.show()
