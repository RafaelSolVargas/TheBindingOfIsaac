from pygame import Rect
from Utils.Hitbox import Hitbox
from Utils.Converter import Converter
from Utils.Movement import GAHandler


class Ataque:
    def __init__(self, ponto_inicial: tuple, pontos_destino: list, alcance: int, dano: int) -> None:
        self.__p1 = ponto_inicial
        self.__pontos_2 = pontos_destino
        self.__alcance = alcance
        self.__dano = dano
        self.__pontos = self.__criar_pontos()

    @property
    def dano(self) -> int:
        return self.__dano

    @property
    def alcance(self) -> int:
        return self.__alcance

    def acertou_hitbox(self, hitbox: Hitbox) -> bool:
        rect = Rect(hitbox.posicao, hitbox.tamanho)
        for ponto in self.__pontos:
            if rect.collidepoint(ponto):
                return True

        return False

    def __criar_pontos(self) -> list:
        pontos = []
        for p2 in self.__pontos_2:
            func = GAHandler.gerar_equação_vetorial_reta(self.__p1, p2)

            x = 0.6
            step = 0.2
            alcance = Converter.alcance_to_vector_dist(self.__alcance)
            while x < alcance:
                ponto = func(x)
                pontos.append(ponto)
                x += step

        return pontos
