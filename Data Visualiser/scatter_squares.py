import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.scatter(x_values,y_values,color = (0.9,0.2,0.5), s=10)
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Kwadraty liczb", fontsize = 24)
ax.set_xlabel("Wartość", fontsize = 14)
ax.set_ylabel("Kwadraty wartości", fontsize =14)

ax.tick_params(labelsize = 14)

ax.ticklabel_format(style='plain')
ax.axis([0, 1100, 0, 1_000_000])

plt.savefig('squares_plot.png')
plt.show()