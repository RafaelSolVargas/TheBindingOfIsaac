from Config.Enums import Dificuldade
from Config.Singleton import Singleton


class Opcoes(Singleton):

    def __init__(self) -> None:
        if not super().created:
            self.__dificuldade = Dificuldade.medio
            self.__nome = 'Tatakae'
            self.__tocar_musica = True
            self.__menor_unidade = 24
            self.__tamanho_tela = (1128, 768)
            self.__TAMANHO_HUD = (1128, 144)
            self.__POSICAO_HUD = (0, 0)
            self.__POSICAO_TELAS = (0, 0)
            self.__POSICAO_MAPAS = (0, 144)
            self.__TAMANHO_MATRIZ_REDUZIDA = (
                1128 / self.__menor_unidade, 624 / self.__menor_unidade)
            self.__TAMANHO_MAPAS = (1128, 624)
            self.__GAME_TITLE = 'The Binding of Isaac'
            self.__MAX_ALCANCE = 3.5
            self.__MIN_ALCANCE = 1.2
            self.__ITENS_DROPPED_DURATION = 500
            self.__MAX_DELAY_ATAQUE = 60
            self.__MIN_DELAY_ATAQUE = 10

    @property
    def tocar_musica(self) -> bool:
        return self.__tocar_musica

    @tocar_musica.setter
    def tocar_musica(self, value) -> None:
        if type(value) == bool:
            self.__tocar_musica = value

    @property
    def dificuldade(self) -> Dificuldade:
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade) -> None:
        if isinstance(dificuldade, Dificuldade):
            self.__dificuldade = dificuldade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, value) -> None:
        if type(value) == str:
            self.__nome = value

    @property
    def TAMANHO_TELA(self) -> tuple:
        return self.__tamanho_tela

    @property
    def MENOR_UNIDADE(self) -> int:
        return self.__menor_unidade

    @property
    def GAME_TITLE(self) -> str:
        return self.__GAME_TITLE

    @property
    def TAMANHO_MAPAS(self) -> int:
        return self.__TAMANHO_MAPAS

    @property
    def POSICAO_MAPAS(self) -> str:
        return self.__POSICAO_MAPAS

    @property
    def TAMANHO_HUD(self) -> int:
        return self.__TAMANHO_HUD

    @property
    def POSICAO_HUD(self) -> str:
        return self.__POSICAO_HUD

    @property
    def MAX_ALCANCE(self) -> int:
        return self.__MAX_ALCANCE

    @property
    def MIN_ALCANCE(self) -> int:
        return self.__MIN_ALCANCE

    @property
    def MAX_DELAY_ATAQUE(self) -> int:
        return self.__MAX_DELAY_ATAQUE

    @property
    def MIN_DELAY_ATAQUE(self) -> int:
        return self.__MIN_DELAY_ATAQUE

    @property
    def ITENS_DROPPED_DURATION(self) -> int:
        return self.__ITENS_DROPPED_DURATION

    @property
    def POSICAO_TELAS(self) -> tuple:
        return self.__POSICAO_TELAS
