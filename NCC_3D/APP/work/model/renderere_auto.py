"""
Created by SungMin Yoon on 2022-09-22..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk


def make_2d_to_3d(path, z_size):

    # jpg file Reader
    Jpg_Reader = vtk.vtkJPEGReader()

    # 디버그 창 끄기
    Jpg_Reader.GlobalWarningDisplayOff()

    # 크기만 있고 방향을 가지지 않는 양 = Scalar
    Jpg_Reader.SetNumberOfScalarComponents(1)

    # It shows that the image is three-dimensional
    Jpg_Reader.SetFileDimensionality(3)

    # Define image size , This line indicates that the image size is （512*512*240）
    Jpg_Reader.SetDataExtent(0, 512, 0, 512, 0, z_size)

    # Set the storage location of the image
    Jpg_Reader.SetFilePrefix(path)

    # Set image prefix name
    # Indicates that the image prefix is a number （ Such as ：0.jpg）
    Jpg_Reader.SetFilePattern("%s%d.jpg")
    Jpg_Reader.Update()
    Jpg_Reader.SetDataByteOrderToLittleEndian()

    # Method of calculating contour
    contour = vtk.vtkMarchingCubes()
    contour.SetInputConnection(Jpg_Reader.GetOutputPort())
    contour.ComputeNormalsOn()
    contour.SetValue(0, 128)

    # 스무딩 필터
    smoothingFilter = vtk.vtkSmoothPolyDataFilter()
    smoothingFilter.SetInputDataObject(contour.GetOutput())
    smoothingFilter.SetNumberOfIterations(10)
    smoothingFilter.SetRelaxationFactor(0.5)
    smoothingFilter.FeatureEdgeSmoothingOff()
    smoothingFilter.BoundarySmoothingOn()
    smoothingFilter.Update()

    normalGenerator = vtk.vtkPolyDataNormals()
    normalGenerator.SetInputConnection(smoothingFilter.GetOutputPort())
    normalGenerator.ComputePointNormalsOn()
    normalGenerator.ComputeCellNormalsOn()
    normalGenerator.Update()

    # mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(contour.GetOutputPort())
    # mapper.ScalarVisibilityOff()

    # 색 변환
    mapper, actor = add_to_renderer(item=contour, color='LightPink', opacity=1)
    actor.SetMapper(mapper)

    return actor


def add_to_renderer(item, color, opacity):

    colors = vtk.vtkNamedColors()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetScalarVisibility(False)

    if hasattr(item, 'GetOutputPort'):
        mapper.SetInputConnection(item.GetOutputPort())
    elif isinstance(item, vtk.vtkPolyData):
        mapper.SetInputData(item)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d(color))
    actor.GetProperty().SetOpacity(opacity)

    return mapper, actor
