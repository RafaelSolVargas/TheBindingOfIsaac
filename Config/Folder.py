from Config.Singleton import Singleton
import os


class Folder(Singleton):
    def __init__(self) -> None:
        current = os.path.dirname(__file__)
        self.assets = self.__get_assets_path(current)
        self.sounds = self.__get_sounds_path(current)
        self.base = self.__get_base_path(current)

    def create_assets_path(self, folders: list, archive=None) -> str:
        new_path = self.assets
        for folder in folders:
            new_path += f'{folder}{os.sep}'

        if archive is not None:
            new_path += archive

        return new_path

    def create_sounds_path(self, folders: list, archive=None) -> str:
        new_path = self.sounds
        for folder in folders:
            new_path += f'{folder}{os.sep}'

        if archive is not None:
            new_path += archive

        return new_path

    def __get_assets_path(self, current: str) -> str:
        last_sep_index = -1
        for x in range(len(current) - 1, -1, -1):
            if current[x] == os.sep:
                last_sep_index = x
                break

        path = current[:last_sep_index] + os.sep + 'Assets' + os.sep
        return path

    def __get_sounds_path(self, current: str) -> str:
        last_sep_index = -1
        for x in range(len(current) - 1, -1, -1):
            if current[x] == os.sep:
                last_sep_index = x
                break

        path = current[:last_sep_index] + os.sep + 'Sounds' + os.sep
        return path

    def __get_base_path(self, current: str) -> str:
        last_sep_index = -1
        for x in range(len(current) - 1, -1, -1):
            if current[x] == os.sep:
                last_sep_index = x
                break
        return current[:last_sep_index] + os.sep
