"""
Created by SungMin Yoon on 2022-11-03..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from PySide6.QtWidgets import *

TITLE_X = 'x :'
TITLE_Y = 'y :'
TITLE_Z = 'z :'
TITLE_SIZE = '---------------------------:'
TITLE_SIZE_SIZE = 'size :'
TITLE_DETAILS_TYPE = 'type :'


class TextBox:

    input_size = None   # 사이즈 입력 합니다.

    def __init__(self):
        print('TextBox: init')
        self.x_box = QHBoxLayout()
        self.y_box = QHBoxLayout()
        self.z_box = QHBoxLayout()
        self.type_box = QHBoxLayout()
        self.size_box = QHBoxLayout()
        self.size_box_s = QHBoxLayout()

    def create(self):
        _panel = QWidget()
        _panel.setFixedSize(115, 200)

        position_x = QLabel(TITLE_X)
        position_y = QLabel(TITLE_Y)
        position_z = QLabel(TITLE_Z)
        line_label = QLabel(TITLE_SIZE)
        size_label_s = QLabel(TITLE_SIZE_SIZE)
        type_label = QLabel(TITLE_DETAILS_TYPE)

        self.x_box.addWidget(position_x)
        self.y_box.addWidget(position_y)
        self.z_box.addWidget(position_z)

        self.size_box_s.addWidget(size_label_s)
        self.size_box.addWidget(line_label)

        self.type_box.addWidget(type_label)

        details_group = QVBoxLayout()
        details_group.addLayout(self.x_box)
        details_group.addLayout(self.y_box)
        details_group.addLayout(self.z_box)
        details_group.addLayout(self.size_box)
        details_group.addLayout(self.size_box_s)
        details_group.addLayout(self.type_box)

        _panel.setLayout(details_group)

        return _panel

