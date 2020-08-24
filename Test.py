import numpy as np

if __name__ == "__main__":
    x = range(0,3)
    y = range(0,5)
    cord = np.meshgrid(x,y, indexing='ij', sparse=False)
    print(cord)
    grid = np.stack(cord, axis=-1)
    print(grid[2])
    print(grid.shape)