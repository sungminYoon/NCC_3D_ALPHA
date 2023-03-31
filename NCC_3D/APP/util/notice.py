"""
Created by SungMin Yoon on 2022-09-19..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

from PySide6.QtWidgets import *


def message(title, msg):
    button_reply = QMessageBox.question(None, title, msg, QMessageBox.Yes)
    if button_reply == QMessageBox.Yes:
        print('Yes clicked.')