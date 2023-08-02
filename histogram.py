import matplotlib.pyplot as plt

# ヒストグラム
x = [1,3,5,7,4,5,6,9]
y = [1,2,3,4,5,6,7,8]

plt.hist(x,y, histtype='bar', rwidth=0.8)
plt.title("Historgram")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.show()