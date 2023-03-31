"""
Created by SungMin Yoon on 2022-05-16..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

from PySide6 import QtCore
from PySide6.QtWidgets import *
from APP.work.provider.container import Container
from APP.work.provider.director import Director
from APP.work.control.vtk_controller import VtkController
from APP.work.view.menu import Menu
from APP.work.view.menu import MenuDelegate
from APP.work.view.property import Property
from APP.work.view.property import PropertyDelegate
from APP.work.view.tool import Tool
from APP.work.view.console import Console


class Window(QWidget, MenuDelegate, PropertyDelegate):

    """UI"""
    menu: Menu              # 좌측 상단 File Menu 버튼 모음 입니다.
    tool: Tool              # 상단 3D 객체의 도구 버튼 모음 입니다.
    console: Console        # 하단 3D 객체 상태 및 시스템 메시지 입니다.
    property: Property      # 우측 3D 객체의 속성및 제어 버튼 모음 입니다.

    """VTK"""
    vtkController: VtkController    # VTK 의 3D 뷰와 객체를 제어 합니다.

    """DATA"""
    container: Container    # Numpy data 기반 좌표로 만든 객체 저장소 입니다.
    director: Director      # 각각의 다른 3D 객체를 생성 합니다.

    """DELEGATE"""
    user_input = None   # Property delegate method
    data_ready = None   # Menu delegate method

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        print('Window: init')
        self.current_target_actor = None

        # 윈도우 세팅
        self.setWindowTitle('NCC 3D Application')
        self.setWindowState(QtCore.Qt.WindowMaximized)

        # 생성 및 delegate 등록
        self.menu = Menu()
        self.menu.delegate = self
        self.menu_file_list = self.data_ready

        self.property = Property()
        self.property.delegate = self
        self.property_user_input = self.user_input
        self.property_user_move = self.user_move

        self.tool = Tool()
        self.console = Console()
        self.container = Container()
        self.director = Director()
        self.vtkController = VtkController()

        # ui
        self.ui_setup()

    def ui_setup(self):
        print('Window: uiSetup')

        # Layout 생성
        form_box = QHBoxLayout()
        _left = QVBoxLayout()
        _top = QVBoxLayout()
        _center = QVBoxLayout()
        _right = QVBoxLayout()
        _bottom = QVBoxLayout()

        # UI 정렬및 입력
        _left.setAlignment(QtCore.Qt.AlignLeft)
        _left.setAlignment(QtCore.Qt.AlignTop)
        _left.addLayout(self.menu)

        _top.addLayout(self.tool)
        _bottom.addLayout(self.console)

        _center.addLayout(_top)
        _center.addWidget(self.vtkController)
        _center.addLayout(_bottom)

        _right.setAlignment(QtCore.Qt.AlignLeft)
        _right.setAlignment(QtCore.Qt.AlignTop)
        _right.addLayout(self.property)

        # 폼 박스에 Layout 배치
        form_box.addLayout(_left)
        form_box.addLayout(_center)
        form_box.addLayout(_right)

        # 화면 보이기
        self.setLayout(form_box)
        self.show()



