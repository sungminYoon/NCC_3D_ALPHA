"""
Created by SungMin Yoon on 2022-05-30..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk
import numpy as np
from PIL import Image
from APP.util import convertor_render


def to_numpy(path):
    '''
    이미지를 VTK 이미지 형식으로 변환
    :param vtk_frame: 보여줄 화면
    :param renderer: 3D 객체
    :param image_path: 이미지 경로
    '''

    # image -> numpy
    array = np.array(Image.open(path))

    # numpy 에서 vtk 이미지로 변경하고
    # vtk.vtkImageData()
    image_vtk = convertor_render.numpy_to_vtk_use(array, True, 'char')
    print(image_vtk)

    # 이미지를 3차원 좌표 객체로 변경 하고
    # Convert the image to a poly data
    imageDataGeometryFilter = vtk.vtkImageDataGeometryFilter()
    imageDataGeometryFilter.SetInputData(image_vtk)
    imageDataGeometryFilter.Update()

    # 3차원 좌표 객체를 면 Mapper 로 변경하고
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(imageDataGeometryFilter.GetOutputPort())

    # 보여줄 actor 객체를 생성 하고
    # actor 에 '면 Mapper' 를 입력하고
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor
