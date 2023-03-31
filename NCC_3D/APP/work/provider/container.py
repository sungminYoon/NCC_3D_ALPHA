"""
Created by SungMin Yoon on 2022-09-01..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import numpy as np
from PIL import Image
from APP.util import create_stl


class Container:

    data = None
    test_arr = None

    def __init__(self):
        pass

    def create_piece(self, file_list):

        path = file_list[0]
        img = Image.open(path)
        binary_np = np.array(img)
        self.data = np.dstack([binary_np] * 1)

        print('Container create_piece = ', self.data.shape)
        create_stl.stl_file(self.data)

    def create_full(self, file_list):

        i = 1
        for path in file_list:

            img = Image.open(path)

            # image 파일을 numpy 로 변환 합니다.
            binary_np = np.array(img)

            # 2차원 stack 쌓아서 3차원 변환
            self.data.shape = np.dstack([binary_np]*i)

            i = i + 1

        print('Container create_full = ', self.data.shape)
        create_stl.stl_file(self.data)

    def create_part(self, file_list):

        self.create_part(file_list)

        h, w, deep = self.data.shape
        print('size = ', h, w, deep)

        # x, y, z 축변환
        for z in range(0, deep):

            position = []
            for x in range(0, w):

                row = []
                column = []
                for y in range(0, h):

                    value = self.data[x][y][z]
                    if 128 > value > 0:
                        column.append(y)

                    _t = (x, column)
                    row.append(_t)

                position.append(row)

            position_np = np.array(position)
            print('shape = ', position_np.shape)

            self.test_arr = np.dstack([position_np]*(z+1))

            if z == 0:
                break

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

