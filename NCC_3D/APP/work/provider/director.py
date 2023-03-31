"""
Created by SungMin Yoon on 2022-06-08..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import threading
from APP.work.model import renderer_mesh
from APP.work.model import renderer_image
from APP.work.model import renderer_title
from APP.work.model import renderer_rectangle
from APP.work.model import renderere_auto
from APP.work.model.object_solid import ObjectSolid


class Director:

    actor_list: list   # 3D 객체들을 생성 후 리스트로 보관 합니다.

    def __init__(self):
        self.actor_list = []

    def object_generator(self, z, folder, frame):

        # 3D 객체를 생성 합니다.
        frame.renderer.AddActor(self.make('Title', None, None))
        frame.renderer.AddActor(self.make('Auto', folder, z))
        # self.make('Image', None)
        # self.make('Mesh', None)

    # 3D 를 랜더링 합니다.
    def make(self, name, active_folder, z_depth):

        _actor = None
        object_solid: ObjectSolid = ObjectSolid()

        if 'Title' == name:
            _actor = renderer_title.set_title("NCC 3D")

        if 'Image' == name:
            _actor = renderer_image.to_numpy('./APP/resource/abc.jpg')

        if 'Mesh' == name:
            _actor = renderer_mesh.to_solid()

        if 'Rectangle' == name:
            _actor = renderer_rectangle.to_grid()

        if 'Auto' == name:

            # 지연 처리
            delay = threading.Event()
            delay_method = threading.Thread(name='block',
                                            target=self.delay_save_actor,
                                            args=[delay, object_solid, _actor])
            delay_method.start()

            # 활성 된 경로의 파일을 solid object 로 변환 합니다.
            object_solid.set_data(active_folder)

            # actor 생성
            _actor = renderere_auto.make_2d_to_3d(active_folder, z_depth)

            # 위 method 가 완료 되면 delay_save_actor method 를 실행 합니다.
            delay.set()

        # 3D _actor 객체를 리스트에 보관 합니다.
        self.actor_list.append(_actor)

        # 3D _actor 프레임 에 넣습니다.
        return _actor

    def delay_save_actor(self, event, object_solid: ObjectSolid, actor):

        # thread 대기
        event.wait()

        # 3d object 객체를 저장 합니다.
        object_solid.set_actor(actor)


