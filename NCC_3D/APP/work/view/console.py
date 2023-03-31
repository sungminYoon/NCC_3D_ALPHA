"""
Created by SungMin Yoon on 2022-09-02..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from PySide6.QtWidgets import *

TITLE_1 = 'message > \n Hello NCC 3D'


class Console(QVBoxLayout):
    console_btn = None

    def __init__(self):
        super().__init__()
        print('Console: init')

        # 변환 그룹
        self.console_group = QVBoxLayout()

        # data 불러 오기 버튼
        self.console_btn = QPushButton(TITLE_1)
        self.console_btn.clicked.connect(self.console_btn_click)
        self.console_btn.setStyleSheet("QPushButton { text-align: left; }")

        self.ui_setup()

    def ui_setup(self):
        # 위젯: 그룹
        self.console_group.addWidget(self.console_btn)

        # 메뉴 그룹을 베이스 Layout 등록 합니다.
        self.addLayout(self.console_group)

    def console_btn_click(self):
        """
        Console(EventMethod): console_btn_click
        :return:
        """
