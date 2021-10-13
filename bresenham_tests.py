import unittest
import notebook_loader
from Bresenham3D import bresenham
import numpy as np


class Bresenham3dTestCase(unittest.TestCase):
    def test_straight_line_along_x(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([0, 1, 2], dtype=np.float32)
        target = np.array([5, 1, 2], dtype=np.float32)
        step_size = 0.5
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 2, 4],
            [1, 2, 4],
            [2, 2, 4],
            [3, 2, 4],
            [4, 2, 4],
            [5, 2, 4],
            [6, 2, 4],
            [7, 2, 4],
            [8, 2, 4],
            [9, 2, 4],
            [10, 2, 4]
        ], dtype=np.float32))), 0)

    def test_straight_line_along_y(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([0, 0, 2], dtype=np.float32)
        target = np.array([0, 5, 2], dtype=np.float32)
        step_size = 0.5
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 0, 4],
            [0, 1, 4],
            [0, 2, 4],
            [0, 3, 4],
            [0, 4, 4],
            [0, 5, 4],
            [0, 6, 4],
            [0, 7, 4],
            [0, 8, 4],
            [0, 9, 4],
            [0, 10, 4]
        ], dtype=np.float32))), 0)

    def test_straight_line_along_z(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([0, 5, 0], dtype=np.float32)
        target = np.array([0, 5, 5], dtype=np.float32)
        step_size = 0.5
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 10, 0],
            [0, 10, 1],
            [0, 10, 2],
            [0, 10, 3],
            [0, 10, 4],
            [0, 10, 5],
            [0, 10, 6],
            [0, 10, 7],
            [0, 10, 8],
            [0, 10, 9],
            [0, 10, 10]
        ], dtype=np.float32))), 0)

    def test_diagonal(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([0, 0, 0], dtype=np.float32)
        target = np.array([5, 5, 5], dtype=np.float32)
        step_size = 0.5
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
            [4, 4, 4],
            [5, 5, 5],
            [6, 6, 6],
            [7, 7, 7],
            [8, 8, 8],
            [9, 9, 9],
            [10, 10, 10]
        ], dtype=np.float32))), 0)

    def test_diagonal_step1(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([0, 0, 0], dtype=np.float32)
        target = np.array([10, 10, 10], dtype=np.float32)
        step_size = 1.0
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
            [4, 4, 4],
            [5, 5, 5],
            [6, 6, 6],
            [7, 7, 7],
            [8, 8, 8],
            [9, 9, 9],
            [10, 10, 10]
        ], dtype=np.float32))), 0)

    def test_diagonal_step2(self):
        a = np.zeros((5, 5, 5), dtype=np.float32)
        start = np.array([0, 0, 0], dtype=np.float32)
        target = np.array([10, 10, 10], dtype=np.float32)
        step_size = 2.0
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
            [4, 4, 4],
            [5, 5, 5]
        ], dtype=np.float32))), 0)

    def test_diagonal_reversed(self):
        a = np.zeros((10, 10, 10), dtype=np.float32)
        start = np.array([5, 5, 5], dtype=np.float32)
        target = np.array([0, 0, 0], dtype=np.float32)
        step_size = 0.5
        voxels = bresenham(start, target, a, step_size=step_size)
        self.assertAlmostEqual(np.max(np.abs(np.array(voxels) - np.array([
            [10, 10, 10],
            [9, 9, 9],
            [8, 8, 8],
            [7, 7, 7],
            [6, 6, 6],
            [5, 5, 5],
            [4, 4, 4],
            [3, 3, 3],
            [2, 2, 2],
            [1, 1, 1],
            [0, 0, 0]
        ], dtype=np.float32))), 0)


if __name__ == '__main__':
    unittest.main()
