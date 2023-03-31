"""
Created by SungMin Yoon on 2022-05-30..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk


class Camera:

    vtk_widget = None

    def __init__(self, vtk_widget):
        super(Camera, self).__init__()
        self.vtk_widget = vtk_widget

    def get_window(self):

        vtk_window = self.vtk_widget.GetRenderWindow()
        inter_actor = vtk_window.GetInteractor()
        inter_actor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        inter_actor.Initialize()

        return vtk_window
