from pygame import Rect, Surface
from Objetos.AbstractObjeto import AbstractObjeto
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite


class ObjetoNaoAnimado(AbstractObjeto):
    __pathname_to_sprite = {}

    def __init__(self, posicao: tuple, tamanho: tuple, transpassavel: bool, bloqueia_visao: bool, path_sprite: str) -> None:
        super().__init__(posicao, tamanho, transpassavel, bloqueia_visao)

        if not path_sprite in ObjetoNaoAnimado.__pathname_to_sprite.keys():
            self.__image = self.__load_sprite(path_sprite)
        else:
            self.__image = import_single_sprite(path_sprite, tamanho)

        self.__rect = self.__image.get_rect(center=self.hitbox.center)

    def desenhar(self, tela: TelaJogo) -> None:
        tela.janela.blit(self.__image, self.__rect)

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    def __load_sprite(self, path) -> Surface:
        image_surf = import_single_sprite(path, self.hitbox.tamanho)
        ObjetoNaoAnimado.__pathname_to_sprite[path] = image_surf
        return image_surf
