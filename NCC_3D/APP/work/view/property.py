"""
Created by SungMin Yoon on 2022-09-02..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from APP.util import cross_button
from APP.oop.text_box import TextBox


class PropertyDelegate:

    # 사용자 선택 변화
    property_user_input = None
    property_user_move = None


class Property(QVBoxLayout):

    delegate: PropertyDelegate = None

    def __init__(self):
        super().__init__()
        print('Control: init')

        cross_button.call_event = self.cross_button_click

        # input data
        self.input_point_x = QLineEdit()
        self.input_point_x.setObjectName('x')
        self.input_point_x.setText('0.0')
        self.input_point_x.setAlignment(Qt.AlignRight)
        self.input_point_x.setStyleSheet("background-color:white;")
        self.input_point_x.setFixedWidth(30)
        self.input_point_x.setFixedHeight(20)
        self.input_point_x.returnPressed.connect(
            lambda stat=False, sender=self.input_point_x: self.line_changed(sender))

        self.input_point_y = QLineEdit()
        self.input_point_y.setObjectName('y')
        self.input_point_y.setText('0.0')
        self.input_point_y.setAlignment(Qt.AlignRight)
        self.input_point_y.setStyleSheet("background-color:white;")
        self.input_point_y.setFixedWidth(30)
        self.input_point_y.setFixedHeight(20)
        self.input_point_y.returnPressed.connect(
            lambda stat=False, sender=self.input_point_y: self.line_changed(sender))

        self.input_point_z = QLineEdit()
        self.input_point_z.setObjectName('z')
        self.input_point_z.setText('0.0')
        self.input_point_z.setAlignment(Qt.AlignRight)
        self.input_point_z.setStyleSheet("background-color:white;")
        self.input_point_z.setFixedWidth(30)
        self.input_point_z.setFixedHeight(20)
        self.input_point_z.returnPressed.connect(
            lambda stat=False, sender=self.input_point_z: self.line_changed(sender))

        self.input_size = QLineEdit()
        self.input_size.setObjectName('s')
        self.input_size.setText('5')
        self.input_size.setAlignment(Qt.AlignRight)
        self.input_size.setStyleSheet("background-color:white;")
        self.input_size.setFixedWidth(30)
        self.input_size.setFixedHeight(20)
        self.input_size.returnPressed.connect(
            lambda stat=False, sender=self.input_size: self.line_changed(sender))

        self.ui_setup()

    def ui_setup(self):
        detail_box = QHBoxLayout()

        # 십자 버튼 생성
        transform_panel = cross_button.create()

        # 객체 명세 생성
        text_box = TextBox()
        details_panel = text_box.create()
        text_box.x_box.addWidget(self.input_point_x)
        text_box.y_box.addWidget(self.input_point_y)
        text_box.z_box.addWidget(self.input_point_z)
        text_box.size_box_s.addWidget(self.input_size)
        detail_box.addWidget(details_panel)

        # 베이스 Layout 등록 합니다.
        self.addWidget(transform_panel)
        self.addLayout(detail_box)

    def line_changed(self, sender: QLineEdit):
        """
        Property(EventMethod): line_changed
        """
        self.delegate.property_user_input(sender)

    def cross_button_click(self, msg):
        """
        Property(EventMethod): cross_button_click
        """
        self.delegate.property_user_move(msg)

    def re_position_text(self, x, y, z):
        print('Property: re_position_text', x, ':', y, ':', z)
        s_x = f'{x}'
        s_y = f'{y}'
        s_z = f'{z}'
        self.input_point_x.setText(s_x)
        self.input_point_y.setText(s_y)
        self.input_point_z.setText(s_z)

    def target_set(self, target_object):
        pass



