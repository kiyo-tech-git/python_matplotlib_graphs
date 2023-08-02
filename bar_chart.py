import matplotlib.pyplot as plt
from matplotlib import style

# 棒グラフ
style.use("ggplot")
x = [1,3,5]
y = [4,5,1]

x2 = [2,4,6]
y2 = [6,3,2]
plt.bar(x,y, label='xy', color="green")
plt.bar(x2,y2, label='x2y2', color="blue")
plt.title("bar_chart")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()

plt.grid(True, color='blue')
plt.show()