"""
Created by SungMin Yoon on 2022-05-31..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import numpy as np
from stl import mesh  # pip install numpy-stl

from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials


def stl_file(data):

    # Define the 8 vertices of the cube
    # vertices = np.array([
    #     [-1, -1, -1],   # 좌 아래 뒤 x y z
    #     [+1, -1, -1],   # 우 아래 뒤
    #     [+1, +1, -1],
    #     [-1, +1, -1],
    #     [-1, -1, +1],
    #     [+1, -1, +1],
    #     [+1, +1, +1],
    #     [-1, +1, +1]])
    #
    # # Define the 12 triangles composing the cube
    # faces = np.array([
    #     [0, 3, 1],
    #     [1, 3, 2],
    #     [0, 4, 7],
    #     [0, 7, 3],
    #     [4, 5, 6],
    #     [4, 6, 7],
    #     [5, 1, 2],
    #     [5, 2, 6],
    #     [2, 3, 6],
    #     [3, 7, 6],
    #     [0, 1, 5],
    #     [0, 5, 4]])
    #
    # # Create the mesh
    # cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    # for i, f in enumerate(faces):
    #     for j in range(3):
    #         # cube.vectors[i][j] = data[f[j], :]
    #         cube.vectors[i][j] = vertices[f[j], :]


    # Write the mesh to file "cube.stl"
    # cube.save('D:\mesh.stl')

    model = VoxelModel(data, generateMaterials(0))
    mesh = Mesh.fromVoxelModel(model)
    mesh.export('D:\mesh.stl')


def rectangle():

    # Define the 8 vertices of the cube
    vertices = np.array([
        [-1, -1, -1],   # 좌 아래 뒤
        [+1, -1, -1],   # 우 아래 뒤
        [+1, +1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
        [+1, -1, +1],
        [+1, +1, +1],
        [-1, +1, +1]])

    # Define the 12 triangles composing the cube
    faces = np.array([
        [0, 3, 1],
        [1, 3, 2],
        [0, 4, 7],
        [0, 7, 3],
        [4, 5, 6],
        [4, 6, 7],
        [5, 1, 2],
        [5, 2, 6],
        [2, 3, 6],
        [3, 7, 6],
        [0, 1, 5],
        [0, 5, 4]])

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    # Write the mesh to file "cube.stl"
    cube.save('././resource/cube.stl')
