from Config.Folder import Folder
from Itens.Pocoes.PocaoGenerica import PocaoGenerica
from Personagens.Status import Status
from pygame import Rect, Surface


class PocaoPequena(PocaoGenerica):
    folder = Folder()
    __PATH = folder.create_assets_path(['pocoes'], 'pocao_pequena.png')
    __SIZE = (30, 30)

    def __init__(self, position=(0, 0)) -> None:
        super().__init__(PocaoPequena.__PATH, PocaoPequena.__SIZE)
        self.__potencia = 3
        self.__pronto = False
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
    def posicao(self, posicao):
        self.__posicao = posicao
        self.__rect = self.__image.get_rect(center=self.__posicao)

    def modificar_status(self, status: Status) -> None:
        if not self.__pronto:
            status.vida += self.__potencia
            self.__pronto = True

    def check_aplicado(self) -> bool:
        return True
