import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
#ax.plot(rw.x_values,rw.y_values,linewidth = 10)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.set_aspect('equal')

#First and last point
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1], c = 'red', edgecolors='none', s=100)

#ax.plot(0, 0, c='green')
#ax.plot(rw.x_values[-1],rw.y_values[-1], c = 'red')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()