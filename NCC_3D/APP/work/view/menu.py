"""
Created by SungMin Yoon on 2022-09-01..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

from PySide6 import QtGui
from PySide6.QtWidgets import *

from PIL import ImageQt
from APP.config.path import local
from APP.util import file_manager

TITLE_DATA_LOAD = '1. Load data'


class MenuDelegate:

    # 사용자 선택 폴더 경로와 파일 list 를 보냅 니다.
    menu_file_list = None


class Menu(QVBoxLayout):
    delegate: MenuDelegate = None

    load_btn = None
    label_logo = None

    def __init__(self):
        super().__init__()
        print('Menu: init')

        # 메뉴 그룹
        self.menu_group = QVBoxLayout()

        # logo 세팅
        qim = ImageQt.ImageQt(local.UI_MENU_LOGO)
        logo_image = QtGui.QPixmap.fromImage(qim)
        logo_image.setDevicePixelRatio(2.5)

        # # logo 라벨
        self.label_logo = QLabel()
        self.label_logo.setScaledContents(True)
        self.label_logo.setPixmap(logo_image)

        # data 불러 오기 버튼
        self.load_btn = QPushButton(TITLE_DATA_LOAD)
        self.load_btn.clicked.connect(self.load_btn_click)
        self.load_btn.setStyleSheet("QPushButton { text-align: left; }")

        self.ui_setup()

    def ui_setup(self):

        # 위젯: 그룹
        self.menu_group.addWidget(self.label_logo)
        self.menu_group.addWidget(self.load_btn)

        # 메뉴 그룹을 베이스 layout 등록 합니다.
        self.addLayout(self.menu_group)

    def load_btn_click(self):
        print('load_btn_click')

        # 데이터 파일 list 저장
        data_file_list = []

        # 경로 가져 오기
        path = file_manager.file_open()
        folder = file_manager.folder_path(path)
        file_list = file_manager.file_list(folder)

        # 데이터 파일 list 만들기
        for name in file_list:
            data_file_name = file_manager.extension_file_check(name)

            if data_file_name is not None:
                data_path = f'{folder}{data_file_name}'
                data_file_list.append(data_path)

        # delegate 를 통해 파일 list 를 넘긴다.
        self.delegate.menu_file_list(data_file_list, folder)

