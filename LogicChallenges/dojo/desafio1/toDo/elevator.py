from time import sleep
from function_elevador import elevador_path, elevador_arrive


class UsuarioElevator:
    def __init__(self, requested_floor: int, up: bool, down: bool, floor_destiny: int):
        self.__requested_floor = requested_floor
        self.up = up
        self.down = down
        self.floor_destiny = floor_destiny

    @property
    def requested_floor(self):
        return self.__requested_floor

    @requested_floor.setter
    def requested_floor(self, valor):
        self.requested_floor = valor


class Elevator:
    def __init__(self, id_elevador: int, localizar: int, ocupado: bool):
        self.id_elevador = id_elevador
        self.localizar = localizar
        self.ocupado = ocupado
        self.user = None

    def busca_andar_solicitado(self):
        floor_pick_up = self.user
        floor_origin = self.localizar

        while floor_origin != floor_pick_up:
            if floor_origin > floor_pick_up:
                floor_origin -= 1
                sleep(1)
                elevador_path()
                print(f"{floor_origin}º")
                sleep(1)





            # Se o andar que o elevador estiver for MENOR do que o usuario o elevador deverá SUBIR até o usuario
            elif floor_origin < floor_pick_up:
                floor_origin += 1
                sleep(0.1)
                elevador_path()

                print(f"{floor_origin}º")
                sleep(0.2)

        elevador_arrive()

    # Levar ao andar desejado
    def leva_andar_desejado(self, andar_destino: int):
        ...


usuario = UsuarioElevator(20, True, False, 12)
elevador = Elevator(10, 40, False)
elevador.user = usuario.requested_floor

elevador.busca_andar_solicitado()
