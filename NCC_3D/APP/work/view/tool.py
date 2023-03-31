"""
Created by SungMin Yoon on 2022-09-02..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from PySide6.QtWidgets import *

TITLE_TOOL = 'TOOL'


class Tool(QVBoxLayout):

    tool_btn = None

    def __init__(self):
        super().__init__()
        print('Tool: init')

        # 변환 그룹
        self.tool_group = QVBoxLayout()

        # data 불러 오기 버튼
        self.tool_btn = QPushButton(TITLE_TOOL)
        self.tool_btn.clicked.connect(self.tool_btn_click)
        self.tool_btn.setStyleSheet("QPushButton { text-align: left; }")

        self.ui_setup()

    def ui_setup(self):

        # 위젯: 그룹
        self.tool_group.addWidget(self.tool_btn)

        # 메뉴 그룹을 베이스 Layout 등록 합니다.
        self.addLayout(self.tool_group)

    def tool_btn_click(self):
        """
        Tool(EventMethod): tool_btn_click
        :return:
        """