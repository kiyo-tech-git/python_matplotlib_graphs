import matplotlib.pyplot as plt
from matplotlib import style

# 折れ線
style.use("ggplot")
x = [1,2,3]
y = [4,5,1]

x2 = [1,2,3]
y2 = [6,3,2]
plt.plot(x,y, 'g', label='xy', linewidth=5)
plt.plot(x2,y2, 'r', label='x2y2', linewidth=5)
plt.title("line_chart")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()

plt.grid(True, color='blue')
plt.show()
