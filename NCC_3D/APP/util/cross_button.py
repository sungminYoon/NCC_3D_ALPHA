"""
Created by SungMin Yoon on 2022-11-03..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from PySide6.QtWidgets import *

TITLE_TRANSFORM_FRONT = 'Re'
TITLE_TRANSFORM_TOP = '↑'
TITLE_TRANSFORM_DEEP = '↓'
TITLE_TRANSFORM_LEFT = '←'
TITLE_TRANSFORM_RIGHT = '→'

call_event = None


def create():
    transform_panel = QWidget()
    transform_panel.setStyleSheet("background-color:lightGray;")
    transform_panel.setFixedSize(130, 130)

    transform_group = QHBoxLayout()
    transform_panel.setLayout(transform_group)

    transform_l = QHBoxLayout()
    transform_v = QVBoxLayout()
    transform_r = QVBoxLayout()

    # object 회전 버튼
    front_btn = QPushButton(TITLE_TRANSFORM_FRONT)
    front_btn.clicked.connect(re_btn_click)
    front_btn.setStyleSheet("QPushButton { text-align: center; }")
    front_btn.setStyleSheet("background-color:darkGray;")
    front_btn.setFixedSize(30, 20)

    top_btn = QPushButton(TITLE_TRANSFORM_TOP)
    top_btn.clicked.connect(up_btn_click)
    top_btn.setStyleSheet("QPushButton { text-align: center; }")
    top_btn.setStyleSheet("background-color:darkGray;")
    top_btn.setFixedSize(30, 20)

    deep_btn = QPushButton(TITLE_TRANSFORM_DEEP)
    deep_btn.clicked.connect(down_btn_click)
    deep_btn.setStyleSheet("QPushButton { text-align: center; }")
    deep_btn.setStyleSheet("background-color:darkGray;")
    deep_btn.setFixedSize(30, 20)

    left_btn = QPushButton(TITLE_TRANSFORM_LEFT)
    left_btn.clicked.connect(left_btn_click)
    left_btn.setStyleSheet("QPushButton { text-align: center; }")
    left_btn.setStyleSheet("background-color:darkGray;")
    left_btn.setFixedSize(30, 20)

    right_btn = QPushButton(TITLE_TRANSFORM_RIGHT)
    right_btn.clicked.connect(right_btn_click)
    right_btn.setStyleSheet("QPushButton { text-align: center; }")
    right_btn.setStyleSheet("background-color:darkGray;")
    right_btn.setFixedSize(30, 20)

    # 위젯: 그룹
    transform_l.addWidget(left_btn)
    transform_v.addWidget(top_btn)
    transform_v.addWidget(front_btn)
    transform_v.addWidget(deep_btn)
    transform_r.addWidget(right_btn)
    transform_group.addLayout(transform_l)
    transform_group.addLayout(transform_v)
    transform_group.addLayout(transform_r)

    return transform_panel


def re_btn_click():
    """
    Property(ButtonEvent method): front_btn_click
    :return:
    """
    print('cross_button: front_btn_click')
    call = call_event
    call('re')


def up_btn_click():
    """
    Property(ButtonEvent method): top_btn_click
    :return:
    """
    print('cross_button: top_btn_click')
    call = call_event
    call('up')


def down_btn_click():
    """
    Property(ButtonEvent method): down_btn_click
    :return:
    """
    print('cross_button: deep_btn_click')
    call = call_event
    call('down')


def left_btn_click():
    """
    Property(ButtonEvent method): left_btn_click
    :return:
    """
    print('cross_button: left_btn_click')
    call = call_event
    call('left')


def right_btn_click():
    """
    Property(ButtonEvent method): right_btn_click
    :return:
    """
    print('cross_button: right_btn_click')
    call = call_event
    call('right')