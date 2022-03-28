from Config.Folder import Folder
from Itens.AbstractItem import AbstractItem
from pygame import Surface
from Utils.Folder import import_single_sprite


class PocaoGenerica(AbstractItem):
    __PATH_TO_SPRITE = {}
    __SIZE_TO_SPRITE = {}
    folder = Folder()
    __GENERIC_POTION_SOUND_PATH = folder.create_sounds_path(['sounds'], 'potions.wav')

    def __init__(self, path: str, size: tuple) -> None:
        if path not in PocaoGenerica.__PATH_TO_SPRITE or size not in PocaoGenerica.__SIZE_TO_SPRITE:
            self.__image = self.__load_image(path, size)
            PocaoGenerica.__PATH_TO_SPRITE[path] = self.__image
            PocaoGenerica.__SIZE_TO_SPRITE[size] = self.__image
        else:
            self.__image = self.__PATH_TO_SPRITE[path]

    def _get_image(self) -> Surface:
        return self.__image

    @classmethod
    def __load_image(cls, path: str, size: tuple) -> Surface:
        return import_single_sprite(path, size)

    @property
    def sound_path(self) -> str:
        return PocaoGenerica.__GENERIC_POTION_SOUND_PATH
