import matplotlib.pyplot as plt

# 積み上げ折れ線グラフ
days = [1,2,3,4,5]

study = [7,8,6,11,7]
eat = [2,3,4,3,2]
work = [7,8,7,2,2]
play = [8,5,7,8,13]

plt.plot([], [], color='m', label='S', linewidth=5)
plt.plot([], [], color='c', label='E', linewidth=5)
plt.plot([], [], color='r', label='W', linewidth=5)
plt.plot([], [], color='k', label='P', linewidth=5)

plt.stackplot(days, study, eat, work, play, colors=['m', 'c', 'r', 'k'])

plt.xlabel("Days")
plt.ylabel("Action")

plt.title("My workdays")
plt.legend()
plt.show()