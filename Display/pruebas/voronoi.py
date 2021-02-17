import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

points = np.array([[0, 3],
                   [0, 1],
                   [2, 5],
                   [2, 1],
                   [1, 4],
                   [7, 8],
                   [7, 6],
                   [7, 4],
                   [8, 5],
                   [6, 3],
                   [4, 5],
                   [4, 3]])
vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.show(fig)
