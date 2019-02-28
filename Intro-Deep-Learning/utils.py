
# coding: utf-8

# In[35]:

get_ipython().magic('matplotlib inline')

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


class Plot:
    
    def __init__(self, labels, xlim, ylim, steps):
        self.labels = labels
        self.xlim = xlim
        self.ylim = ylim
        self.steps = steps
        self.elev = None
        self.azim = None
    
    def coords(self):
        x = np.linspace(self.xlim[0], self.xlim[1], self.steps)
        y = np.linspace(self.ylim[0], self.ylim[1], self.steps)
        self.x, self.y = np.meshgrid(x, y)
        return np.vstack([np.ravel(self.x), np.ravel(self.y)])
    
    def view(self, elev=None, azim=None):
        if elev:
            self.elev = elev
        if azim:
            self.azim = azim
            
    def save(self, path, transparent=True):
        plt.savefig(path, bbox_inches='tight', pad_inches=0.5, transparent=transparent)

    def __call__(self, title, z, cmap=cm.jet, linewidth=0):
        self.fig = plt.figure(figsize=(12, 8), dpi=80,)
        ax = self.fig.gca(projection='3d')
        ax.set_title(title)
        ax.set_xlabel(self.labels[0])
        ax.set_ylabel(self.labels[1])
        ax.set_zlabel(self.labels[2])
        ax.set_xlim(*self.xlim)
        ax.set_ylim(*self.ylim)
        ax.set_zlim(z.min(), z.max())
        ax.view_init(self.elev, self.azim)
        z = z.reshape(self.x.shape)
        ax.plot_surface(self.x, self.y, z, rstride=1, cstride=1, cmap=cmap, linewidth=linewidth)

