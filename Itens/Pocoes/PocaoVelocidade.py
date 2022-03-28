from Config.Folder import Folder
from Itens.Pocoes.PocaoGenerica import PocaoGenerica
from Personagens.Status import Status
from pygame import Rect, Surface


class PocaoVelocidade(PocaoGenerica):
    folder = Folder()
    __PATH = folder.create_assets_path(['pocoes'], 'pocao_velocidade.png')
    __SIZE = (30, 30)

    def __init__(self, position=(0, 0)) -> None:
        super().__init__(PocaoVelocidade.__PATH, PocaoVelocidade.__SIZE)
        self.__status: Status = None
        self.__potencia = 1
        self.__pronto = False
        self.__aplicado = False
        self.__BUFF_TIMER = 800
        self.__posicao = position
        self.__image = self._get_image()
        self.__rect = self.__image.get_rect(center=self.__posicao)

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao) -> tuple:
        self.__posicao = posicao
        self.__rect = self.__image.get_rect(center=self.__posicao)

    def modificar_status(self, status: Status) -> None:
        if not self.__aplicado:
            self.__status = status
            self.__status.vel += self.__potencia
            self.__aplicado = True

    def check_aplicado(self) -> bool:
        if self.__pronto:
            self.__remover_status()
            return True
        else:
            self.__update_timer()
            return False

    def __remover_status(self) -> None:
        self.__status.vel -= self.__potencia

    def __update_timer(self) -> None:
        if self.__BUFF_TIMER > 0:
            self.__BUFF_TIMER -= 1
        else:
            self.__pronto = True
