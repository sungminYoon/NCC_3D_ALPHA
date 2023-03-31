"""
Created by SungMin Yoon on 2022-05-31..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk
import time
from APP.util import create_stl


def to_solid():
    print('obj_mesh: to_solid')

    # create_stl.rectangle()
    # time.sleep(0.1)
    # filenameSTL = '././resource/cube.stl'
    filenameSTL = 'D:\mesh.stl'
    readerSTL = vtk.vtkSTLReader()
    readerSTL.SetFileName(filenameSTL)
    readerSTL.Update()
    poly_data = readerSTL .GetOutput()

    # stl 데이터 체크
    if poly_data.GetNumberOfPoints() == 0:
        raise ValueError("No point data could be loaded from '" + filenameSTL)

    poly_data.ShallowCopy(readerSTL.GetOutput())
    append_filter = vtk.vtkAppendPolyData()
    append_filter.SetInputData(poly_data)
    append_filter.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(append_filter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # 색 변환
    actor.GetProperty().SetColor(0.5, 0.5, 1.0)

    return actor

