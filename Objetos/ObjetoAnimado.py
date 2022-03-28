from pygame import Rect, Surface
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_folder
from Objetos.AbstractObjeto import AbstractObjeto


class ObjetoAnimado(AbstractObjeto):
    __folderpath_to_sprite = {}

    def __init__(self, posicao: tuple, tamanho: tuple, transpassavel: bool, bloqueia_visao: bool, folder_path: str) -> None:
        super().__init__(posicao, tamanho, transpassavel, bloqueia_visao)

        if not folder_path in ObjetoAnimado.__folderpath_to_sprite.keys():
            self.__animation = ObjetoAnimado.__load_sprite(folder_path)
        else:
            self.__animation = ObjetoAnimado.__folderpath_to_sprite[folder_path]

        self.__image = self.__animation[0]
        self.__rect = self.__image.get_rect(center=self.hitbox.center)
        self.__frame_index = 0
        self.__frame_speed = 0.35

    def desenhar(self, tela: TelaJogo) -> None:
        self.__animate()
        tela.janela.blit(self.__image, self.__rect)

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    def __animate(self) -> None:
        self.__image = self.__animation[int(self.__frame_index)]
        self.__rect = self.__image.get_rect(center=self.hitbox.center)

        self.__frame_index += self.__frame_speed
        if self.__frame_index >= len(self.__animation):
            self.__frame_index = 0

    def __load_sprite(self, folder_path) -> Surface:
        image_surf = import_folder(folder_path, self.hitbox.tamanho)
        ObjetoAnimado.__folderpath_to_sprite[folder_path] = image_surf
        return image_surf
