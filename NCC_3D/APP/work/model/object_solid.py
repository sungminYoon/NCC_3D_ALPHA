"""
Created by SungMin Yoon on 2022-09-27..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import os
from APP.util import file_manager


class ObjectSolid:

    actor = None

    def __init__(self):
        pass

    def set_actor(self, actor):
        print('ObjectSolid: set_actor')
        self.actor = actor

    @ classmethod
    def set_data(cls, folder_path):

        # 선택 한 폴더의 jpg 파일만 불러 옵니다.
        file_list = file_manager.file_extension_list(folder_path, 'jpg')

        # 파일 이름을 정렬 합니다.
        file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        # 파일 이름이 0 번 확인
        check_str = file_list[0]
        file_name = check_str.split('.')
        name = file_name[0]

        if name is not '0':

            # 파일 이름 일괄 편집
            i = 0
            for name in file_list:
                src = os.path.join(folder_path, name)
                dst = str(i) + '.jpg'
                dst = os.path.join(folder_path, dst)
                os.rename(src, dst)
                i += 1

