"""
Created by SungMin Yoon on 2022-05-16..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""

import sys
from PySide6.QtWidgets import QApplication
from APP.work.window import Window
from APP.work.window_method import WindowMethod


if __name__ == '__main__':
    print('main')

    app = QApplication(sys.argv)
    window: Window = WindowMethod()
    sys.exit(app.exec())
