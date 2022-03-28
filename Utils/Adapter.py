from Config.Opcoes import Opcoes
from Config.Singleton import Singleton


class Adapter(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__opcoes = Opcoes()

    def pygame_pos_to_matrix_index(self, position: tuple) -> tuple:
        position = self.__remove_offset_from_point(position)
        position = self.__inverter_ponto(position)
        position = self.__reduzir_ponto(position)

        return position

    def matrix_index_to_pygame_pos(self, position: tuple) -> tuple:
        position = self.__aumentar_ponto(position)
        position = self.__inverter_ponto(position)
        position = self.__apply_offset_to_point(position)

        return position

    def matrix_index_list_to_pygame_pos_list(self, list: list) -> list:
        changed_list = []
        for position in list:
            changed_list.append(self.matrix_index_to_pygame_pos(position))
        return changed_list

    def pygame_pos_list_to_matrix_index_list(self, list: list) -> list:
        changed_list = []
        for position in list:
            changed_list.append(self.pygame_pos_to_matrix_index(position))
        return changed_list

    def __inverter_ponto(self, position: tuple) -> tuple:
        return (position[1], position[0])

    def __remove_offset_from_point(self, ponto: tuple) -> tuple:
        return (ponto[0], ponto[1] - self.__opcoes.POSICAO_MAPAS[1])

    def __apply_offset_to_point(self, position: tuple) -> tuple:
        return (position[0], position[1] + self.__opcoes.POSICAO_MAPAS[1])

    def __reduzir_ponto(self, ponto: tuple) -> tuple:
        x = ponto[0] // self.__opcoes.MENOR_UNIDADE
        y = ponto[1] // self.__opcoes.MENOR_UNIDADE

        return (int(x), int(y))

    def __aumentar_ponto(self, ponto: tuple) -> tuple:
        x = ponto[0] * self.__opcoes.MENOR_UNIDADE
        y = ponto[1] * self.__opcoes.MENOR_UNIDADE

        return (x, y)
