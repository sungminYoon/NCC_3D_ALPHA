"""
Created by SungMin Yoon on 2022-05-24..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

import vtk


def set_title(title):
    '''
    VTK 타이틀 UI
    :param vtk_frame: 보여줄 화면
    :param renderer: 3D 객체
    :param title: 제목
    :return: title_actor
    '''

    title_actor = vtk.vtkTextActor()
    title_actor.GetTextProperty().SetFontFamilyAsString("Georgia")
    title_actor.GetTextProperty().SetFontSize(30)
    title_actor.GetTextProperty().SetColor([0, 1, 0]) # R, G, B
    title_actor.SetInput(title)
    title_actor.SetPosition(0, 0)

    return title_actor

