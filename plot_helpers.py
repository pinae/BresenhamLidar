from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def voxel_lines(v, step_size):
    xl = [v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2 + step_size,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2,
          v[0] * step_size - step_size / 2]
    yl = [v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2 + step_size,
          v[1] * step_size - step_size / 2]
    zl = [v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2,
          v[2] * step_size - step_size / 2 + step_size,
          v[2] * step_size - step_size / 2 + step_size]
    return xl, yl, zl


def plot_voxel_line(voxels, step_size, a, start, target):
    fig = plt.figure(figsize=[9.5, 8])
    ax = plt.axes(projection='3d', box_aspect=(1.0, 1.0, 1.0))
    ax.set_xlim3d(0, a.shape[0] * step_size)
    ax.set_xlabel('x')
    ax.set_ylim3d(0, a.shape[1] * step_size)
    ax.set_ylabel('y')
    ax.set_zlim3d(0, a.shape[2] * step_size)
    ax.set_zlabel('z')
    ax.plot3D(*np.column_stack([start, target]), 'red')
    # ax.scatter3D(*np.column_stack([start_voxel*step_size, start_voxel*step_size+0.5]))
    for v in voxels:
        ax.plot3D(*voxel_lines(v, step_size), 'blue')
    # ax.plot3D(*voxel_lines(np.array([0, 0, 0]), step_size), 'green')
    return fig
