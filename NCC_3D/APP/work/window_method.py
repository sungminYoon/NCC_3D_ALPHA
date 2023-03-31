"""
Created by SungMin Yoon on 2022-09-20..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
from .window import Window


class WindowMethod(Window):

    def __init__(self, parent=None):
        super(WindowMethod, self).__init__(parent)
        print('WindowMethod: init')

        self.current_target_actor = None  # 현재 활성 actor

    def data_ready(self, count, folder):
        """
        Window(MenuDelegate): data_ready
        :param count: file list count
        :param folder: user select folder
        :return:
        """

        # 2D -> 3D 생성시 2D Image 의 count 에 따라 z 값을 정함.
        z = len(count)
        self.director.object_generator(z, folder, self.vtkController)
        self.current_target_actor = self.director.actor_list[1]
        self.re_size(1, 1, 5)
        self.rotate(-90)
        self.vtkController.renderer_register()

    # 명세 영역 사용자 입력 3D 모델 객체 변화
    def user_input(self, sender):
        """
        Window(PropertyDelegate): user_input
        :param sender: user input value
        :return:
        """

        # float casting
        value = float(sender.text())

        # delegate 를 통해 input_size 를 send 합니다.
        if sender.objectName() is 'x':
            self.re_point(value, 0, 0)

        if sender.objectName() is 'y':
            self.re_point(0, value, 0)

        if sender.objectName() is 'z':
            self.re_point(0, 0, value)

        if sender.objectName() is 's':  # size
            self.re_size(1, 1, value)

        self.send_object()

    # 사용자 선택 3D 객체 이동 및 표시
    def user_move(self, msg):
        """
        Window(PropertyDelegate): user_move
        :param msg: user click move
        :return:
        """

        position = self.current_target_actor.GetPosition()
        x = position[0]
        y = position[1]
        z = position[2]

        if msg is 'up':
            y = position[1] + 1
            self.re_point(position[0], y, position[2])

        if msg is 'left':
            x = position[0] - 1
            self.re_point(x, position[1], position[2])

        if msg is 'right':
            x = position[0] + 1
            self.re_point(x, position[1], position[2])

        if msg is 'down':
            y = position[1] - 1
            self.re_point(position[0], y, position[2])

        if msg is 're':
            x = 0
            y = 0
            z = 0
            self.re_point(0, 0, 0)

        # 명세 영역 텍스트 변경 표시
        self.property.re_position_text(x, y, z)

    # 현재 선택 된 3D 객체 send.
    def send_object(self):
        self.property.target_set(self.current_target_actor)

    # 현재 선택 된 3D 객체의 위치를 변경 합니다.
    def re_point(self, x, y, z):

        # 위치 변경
        self.current_target_actor.SetPosition(x, y, z)

        # 화면 다시 그리기
        self.vtkController.vtk_view.Render()

    def rotate(self, angle):
        """Rotate around an arbitrary `axis` passing through `axis_point`."""
        axis = (1, 0, 0)
        self.current_target_actor.RotateWXYZ(angle, axis[0], axis[1], axis[2])

        # 화면 다시 그리기
        self.vtkController.vtk_view.Render()

    def re_point_text(self, x, y):

        # 위치 변경
        self.current_target_actor.SetPosition(x, y)

        # 화면 다시 그리기
        self.vtkController.vtk_view.Render()

    # 3D 객체의 크기를 변경 합니다.
    def re_size(self, a, s, b):
        print('WindowMethod: re_size ', a, ':', s, ':', b)
        self.current_target_actor.SetScale(a, s, b)

        # 화면 다시 그리기
        self.vtkController.vtk_view.Render()

    def get_camera(self):
        camera = self.vtkController.renderer.GetActiveCamera()
        print(camera)


