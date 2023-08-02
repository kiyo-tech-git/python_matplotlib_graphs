import matplotlib.pyplot as plt
from matplotlib import style

# 散布図
x = [1,3,5,7,4,5,6,9]
y = [1,2,3,4,5,6,7,8]

plt.scatter(x,y, label='position', color='g', s=25, marker='o')
plt.title("scatter plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()

plt.show()