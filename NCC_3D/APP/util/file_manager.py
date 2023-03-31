"""
Created by SungMin Yoon on 2022-09-19..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import os
import time
import errno
import datetime
import zipfile as compression

from datetime import datetime
from PySide6.QtWidgets import *
from APP.util import notice


def file_open():
    full_path = QFileDialog.getOpenFileName(None, 'Open file', '/')

    file_path = f'{full_path[0]}'
    result = extension_file_check(file_path)

    if result is None:
        notice.message('Warning', 'DATA 가 있는 폴더 에서 파일을 선택 하세요.')

    else:
        return result


# 파일 확장자 채크
def extension_file_check(file_path: str):
    split_list = file_path.split('.')

    # 지원 형식
    extension = (['jpeg', 'jpg', 'png'])

    # 마지막 인자의 교집 합으로 확장자 확인 합니다.
    last_name = ([split_list[-1]])
    intersection = list(set(extension) & set(last_name))
    count: int = len(intersection)

    if count == 0:
        return None
    else:
        return file_path


def auto_open(path):
    QFileDialog.getOpenFileName(None, 'Open file', path)


# 사용자 선택한 폴더 경로를 가져 옵니다.
def open_folder():
    # 사용자 선택한 파일 경로
    file_path = file_open()

    if file_path is 0:
        return

    # 사용자 선택한 경로
    last_name = file_path[file_path.rfind('/') + 1:]
    _, file_extension = os.path.splitext(last_name)

    # 사용자 선택한 폴더 이름
    o_folder = file_path.replace(last_name, '', 1)

    # 폴더 경로 반환
    return o_folder


def get_name(file_name):
    # 파일 이름만 가져 오기
    if file_name.count(".") == 1:  # . 이 한개 일떄
        v = file_name.split(".")
        print("file Name : " + v[0])

    return v[0]


# 경로 에서 폴더 경로만 추출
def folder_path(path: str):

    f = None

    try:
        # / 문자열 구분
        v = path.split("/")

        # 파일명 지우기
        f = path.strip(v[-1])

    except AttributeError as e:
        print(e)

    return f


# 경로 에서 폴더 이름만 추출
def folder_name(path):
    # / 문자열 구분
    v = path.split("/")

    # 문자 열을 뒤에서 부터 읽을때 비어 있지 않으면 값 리턴
    for i in range(1, len(v)):
        str_name = v[-i]
        if str_name != '':
            return str_name
        else:
            pass


# 폴더의 파일 list 를 가지고 옵니다.
def file_list(_folder_path):
    _list = os.listdir(_folder_path)
    return _list


# 폴더의 json 파일 list 를 가지고 옵니다.
def file_json_list(_folder_path):
    file_name_list = os.listdir(_folder_path)
    json_list = [file for file in file_name_list if file.endswith(".json")]
    return json_list


# 폴더의 해당 학장자 파일 list 를 가지고 옵니다.
def file_extension_list(_folder_path, extension):
    file_name_list = os.listdir(_folder_path)
    file_list_png = [file for file in file_name_list if file.endswith(extension)]
    return file_list_png


# 원본 이미지 압축 하기
def image_compression(ori, mask, zipfile):
    with compression.ZipFile(zipfile, mode='w') as f:
        f.write(ori, compress_type=compression.ZIP_DEFLATED)

    # append 압축 파일에 또 다른 파일 추가 마스크 이미지 압축 하기
    with compression.ZipFile(zipfile, mode='a') as f:
        f.write(mask, compress_type=compression.ZIP_DEFLATED)
    print('file_manager: 이미지 압축 완료')


# 압축된 이미지 불러 오기
def load_zip(zip_path, save_path):
    print('file_manager: load_zip')
    full_name = zip_path[zip_path.rfind('/') + 1:]
    folder_name_zip = full_name.replace(".zip", "")

    # zip 파일 인지 확인
    filename, file_extension = os.path.splitext(full_name)
    if file_extension != '.zip':
        print('zip 파일이 아닙 니다.')
        return 0

    path = f'{save_path}{folder_name_zip}'

    zip_image = compression.ZipFile(zip_path)
    zip_image.extractall(path)

    # 하드에 이미지 저장할 시간을 좀 주고
    time.sleep(0.1)
    print('압축 풀기 완료')

    # 압축을 풀어 넣은 경로와 파일 이름을 리턴 합니다.
    simplify_path = f'{path}/'
    ori_name = f'ori_{filename}.png'
    mask_name = f'mask_{filename}.png'
    return simplify_path, ori_name, mask_name


# 저장할 폴더 만들기
def make_folder(folder_path_str):
    if not os.path.isdir(folder_path_str):
        os.makedirs(folder_path_str)


# 날짜 이름 폴더 만들기
def make_folder_date(folder_path_str):
    _name = datetime.today().strftime("%Y%m%d%H%M%S")
    day_folder = f'{folder_path_str}{_name}'
    create_folder(day_folder)
    return day_folder


# 폴더 생성
def create_folder(path):
    try:
        if not (os.path.isdir(path)):
            os.makedirs(os.path.join(path))
            return path
        return path

    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Error to create roi_folder directory!")
            raise


# 상대 경로
def relative_path(full_path, start_name):
    folder_list = full_path.split('/')
    string_path = []

    try:
        index = folder_list.index(start_name)

        i = 0
        for name in folder_list:
            if i > index:
                string_path.append('/')
                string_path.append(name)
            i = i + 1

        # list 를 문자를 -> 문자 열로 변환 합니다.
        string_path = ''.join(string_path)
        result_path = f'{start_name}{string_path}'
        print('file_manager: relative_path = ', result_path)
        return result_path

    except OSError as e:
        if e.errno != errno.EEXIST:
            print('ERROR: relative_path')
            raise
