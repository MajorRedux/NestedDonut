import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

size = 0.3
vals1 = np.array([[1.], [1.], [1.]])
vals2 = np.array([[1.,1.], [1.,1.], [1.,1.]])
vals3 = np.array([[1.,1.,1.,], [1.,1.,1.], [1.,1.,1.]])
vals4 = np.array([[1.,1.,1.,1.], [1.,1.,1.,1.], [1.,1.,1.,1.]])
vals5 = np.array([[1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.]])
vals6 = np.array([[1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.]])
vals7 = np.array([[1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.]])
vals8 = np.array([[1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.]])
vals9 = np.array([[1.,1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.,1.]])
vals10 = np.array([[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.,1.,1.], [1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]])

cmap = plt.get_cmap("tab20c")
inner_colors = cmap(np.arange(3)*4)
outer_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(vals1.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

ax.pie(vals2.flatten(), radius=1.2-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'),startangle=0)

ax.pie(vals3.flatten(), radius=1.4-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

ax.pie(vals4.flatten(), radius=1.6-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'), startangle=135)

ax.pie(vals5.flatten(), radius=1.8-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'), startangle=90)

ax.pie(vals6.flatten(), radius=2-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals7.flatten(), radius=2.2-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'),startangle=90)

ax.pie(vals8.flatten(), radius=2.4-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'),startangle=112.5)

ax.pie(vals9.flatten(), radius=2.6-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'),startangle=90)

ax.pie(vals10.flatten(), radius=2.8-size, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))

plt.show()
