import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
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
triangulation = Delaunay(points)

plt.triplot(points[:, 0], points[:, 1], triangulation.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
