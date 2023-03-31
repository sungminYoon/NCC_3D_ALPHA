"""
Created by SungMin Yoon on 2022-05-20..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

import vtk
import vtkmodules.qt
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import *
from APP.work.view.camera import Camera

vtkmodules.qt.PyQtImpl = "PySide6"
vtkmodules.qt.QVTKRWIBase = "QWidget"


class VtkController(QFrame):

    def __init__(self):
        super(VtkController, self).__init__()

        # Create a VTK widget and add it to the QFrame.
        self.setLayout(QVBoxLayout())
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.layout().addWidget(self.vtk_widget)
        self.layout().setContentsMargins(0, 0, 0, 0)

        # Get the render window and set an inter_actor.
        self.vtk_view = Camera(self.vtk_widget).get_window()

        # Create a new renderer and set the background color.
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground([0.5, 0.5, 0.5])

    # 3D 모델 객체를 등록 합니다.
    def renderer_register(self):

        # 생성한 객체를 VIEW 에 등록 합니다.
        self.vtk_view.AddRenderer(self.renderer)

    def resizeEvent(self, new_size):
        """
        VtkController(EventMethod): resizeEvent
        :param new_size:
        :return:
        """
