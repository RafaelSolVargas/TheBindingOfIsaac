import os
import pickle
from typing import Any
from Config.Singleton import Singleton
from Config.Folder import Folder


class DAO(Singleton):
    def __init__(self, path=None) -> None:
        if not super().created:
            if path is None:
                folder = Folder()
                path = f'{folder.base}DAO{os.sep}saves{os.sep}saves'
            self.__connected = False
            self.__path = path
            self.__cache = {}

            try:
                self.__load()
                print(f'Arquivo {path}.pkl aberto com sucesso')
            except:
                self.__dump()
                print('Erro na hora de abrir o arquivo, tente outro nome')

    @property
    def connected(self) -> bool:
        return self.__connected

    def __dump(self) -> None:
        try:
            with open(f'{self.__path}.pkl', 'wb') as file:
                pickle.dump(self.__cache, file)
        except Exception as e:
            print(e)

    def __load(self):
        with open(f'{self.__path}.pkl', 'rb') as file:
            self.__cache = pickle.load(file)

    def get_all(self) -> dict:
        self.__load()
        return self.__cache

    def add(self, key, value) -> None:
        self.__cache[key] = value
        self.__dump()

    def get(self, key) -> Any:
        if key in self.__cache:
            return self.__cache[key]
        self.__load()
        if key in self.__cache:
            return self.__cache[key]
        return None

    def remove(self, key) -> None:
        if key in self.__cache:
            self.__cache.pop(key)
            self.__dump()
