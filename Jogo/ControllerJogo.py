from typing import List
from Config.Singleton import Singleton
from DAO.JogoDAO import JogoDAO
from Jogo.Jogo import Jogo


class ControllerJogo(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__new_game_name = 'Save1'
            self.__load_game_name = ''
            self.__current_game_save = ''
            self.__dao = JogoDAO()
            self.__current_game = None

    def save(self) -> None:
        self.__dao.add(self.__current_game)

    def create_new_game(self) -> None:
        self.__current_game = Jogo(self.__new_game_name)
        self.__current_game_save = self.__new_game_name

    def load_game(self) -> None:
        self.__current_game = self.__dao.get(self.__load_game_name)
        self.__current_game_save = self.__load_game_name

    def current_game(self) -> Jogo:
        return self.__current_game

    @property
    def new_game_name(self) -> str:
        return self.__new_game_name

    @new_game_name.setter
    def new_game_name(self, value: str) -> None:
        if type(value) == str:
            self.__new_game_name = value

    @property
    def load_game_name(self) -> str:
        return self.__load_game_name

    @load_game_name.setter
    def load_game_name(self, value: str) -> None:
        if type(value) == str:
            self.__load_game_name = value

    @property
    def current_game_save(self) -> str:
        return self.__current_game_save

    @current_game_save.setter
    def current_game_save(self, value: str) -> None:
        if type(value) == str:
            self.__current_game_save = value

    def get_all_names(self) -> List[str]:
        saves = self.__dao.get_all()
        names = list(saves.keys())

        if len(names) < 5:
            diff = 5 - len(names)
            for _ in range(diff):
                names.append('Empty')

        return names[:5]
