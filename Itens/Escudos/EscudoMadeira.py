from pygame import Rect
from Config.Enums import Direction
from Itens.Escudos.AbstractEscudo import AbstractEscudo
from Utils.Hitbox import Hitbox


class EscudoMadeira(AbstractEscudo):
    __DEFESA = 3
    __VIDA = 20
    __REGENERATION_RATE = 1
    __REGENERATION_DELAY = 200
    __MOVEMENT_SLOW = 1

    def __init__(self, player_hitbox: Hitbox) -> None:
        self.__defesa = EscudoMadeira.__DEFESA
        self.__vida = EscudoMadeira.__VIDA
        self.__hitbox = player_hitbox
        self.__delay = EscudoMadeira.__REGENERATION_DELAY

    def update(self):
        if self.__delay > 0:
            self.__delay -= 1
        else:
            if self.__vida < EscudoMadeira.__VIDA:
                self.__vida += EscudoMadeira.__REGENERATION_RATE
                if self.__vida > EscudoMadeira.__VIDA:
                    self.__vida = EscudoMadeira.__VIDA

    def tomar_dano(self, dano) -> int:
        self.__delay = EscudoMadeira.__REGENERATION_DELAY

        dano_real = dano - self.__defesa
        if dano_real < 0:
            return 0

        if self.__vida >= dano_real:
            self.__vida -= dano_real
            return 0
        elif self.__vida > 0:
            dano_nao_defendido = dano_real - self.__vida
            self.__vida = 0
            return dano_nao_defendido
        else:
            return dano

    def hitbox(self, direction: Direction) -> Hitbox:
        direita = [Direction.DIREITA_BAIXO, Direction.DIREITA_CIMA, Direction.DIREITA_MEIO]
        esquerda = [Direction.ESQUERDA_BAIXO, Direction.ESQUERDA_MEIO, Direction.ESQUERDA_CIMA]

        if direction in direita:
            return Hitbox(self.__hitbox.topright, (4, self.__hitbox.altura))
        elif direction in esquerda:
            return Hitbox(self.__hitbox.topleft, (4, self.__hitbox.altura))
        elif direction == Direction.MEIO_CIMA:
            return Hitbox(self.__hitbox.topleft, (self.__hitbox.largura, 4))
        else:
            return Hitbox(self.__hitbox.bottomleft, (self.__hitbox.largura, 4))

    @property
    def movement_slow(self) -> int:
        return EscudoMadeira.__MOVEMENT_SLOW

    @property
    def vida_maxima(self) -> int:
        return EscudoMadeira.__VIDA

    @property
    def vida(self) -> int:
        return self.__vida

    @property
    def defesa(self) -> int:
        return self.__defesa

    @property
    def quebrado(self) -> bool:
        if self.__vida <= 0:
            return True
        else:
            return False
