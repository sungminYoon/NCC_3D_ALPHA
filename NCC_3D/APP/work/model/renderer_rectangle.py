"""
Created by SungMin Yoon on 2022-05-30..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk
import numpy as np

from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkExplicitStructuredGrid
)
from vtkmodules.vtkFiltersCore import (
    vtkExplicitStructuredGridToUnstructuredGrid,
    vtkUnstructuredGridToExplicitStructuredGrid
)


def to_grid():
    print('obj_numpy: to_grid')

    '''
    grid 면적(x,y,z) 간격(x,y,z)
    '''
    grid = create_explicit_structured_grid((10, 10, 10), (1, 1, 1))
    grid = convert_to_unstructured_grid(grid)
    grid = convert_to_explicit_structured_grid(grid)

    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(grid)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


def create_explicit_structured_grid(dimensions, spacing=(1, 1, 1)):
    """Create an explicit structured grid.

    Parameters
    ----------
    dimensions : tuple(int, int, int)
        The number of points in the I, J and K directions.
    spacing : tuple(int, int, int)
        The spacing between points in the I, J and K directions.

    Returns
    -------
    grid : vtkExplicitStructuredGrid
        An explicit structured grid.

    """
    ni, nj, nk = dimensions
    si, sj, sk = spacing

    points = vtkPoints()
    for z in range(0, nk * sk, sk):
        for y in range(0, nj * sj, sj):
            for x in range(0, ni * si, si):
                points.InsertNextPoint((x, y, z))

    cells = vtkCellArray()
    for k in range(0, nk - 1):
        for j in range(0, nj - 1):
            for i in range(0, ni - 1):
                multi_index = ([i, i + 1, i + 1, i, i, i + 1, i + 1, i],
                               [j, j, j + 1, j + 1, j, j, j + 1, j + 1],
                               [k, k, k, k, k + 1, k + 1, k + 1, k + 1])
                pts = np.ravel_multi_index(multi_index, dimensions, order='F')
                cells.InsertNextCell(8, pts)

    grid = vtkExplicitStructuredGrid()
    grid.SetDimensions(ni, nj, nk)
    print('points', points)
    grid.SetPoints(points)
    grid.SetCells(cells)
    return grid


def convert_to_unstructured_grid(grid):
    """Convert explicit structured grid to unstructured grid.

    Parameters
    ----------
    grid : vtkExplicitStructuredGrid
        An explicit structured grid.

    Returns
    -------
    vtkUnstructuredGrid
        An unstructured grid.

    """
    converter = vtkExplicitStructuredGridToUnstructuredGrid()
    converter.SetInputData(grid)
    converter.Update()
    return converter.GetOutput()


def convert_to_explicit_structured_grid(grid):
    """Convert unstructured grid to explicit structured grid.

    Parameters
    ----------
    grid : UnstructuredGrid
        An unstructured grid.

    Returns
    -------
    vtkExplicitStructuredGrid
        An explicit structured grid. The ``'BLOCK_I'``, ``'BLOCK_J'`` and
        ``'BLOCK_K'`` cell arrays are required.

    """
    converter = vtkUnstructuredGridToExplicitStructuredGrid()
    converter.SetInputData(grid)
    converter.SetInputArrayToProcess(0, 0, 0, 1, 'BLOCK_I')
    converter.SetInputArrayToProcess(1, 0, 0, 1, 'BLOCK_J')
    converter.SetInputArrayToProcess(2, 0, 0, 1, 'BLOCK_K')
    converter.Update()
    return converter.GetOutput()






