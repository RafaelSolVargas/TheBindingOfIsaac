from abc import ABC, abstractmethod

from pygame import Rect, Surface
from Config.Enums import Direction
from Itens.Armas.AbstractArma import AbstractArma
from Utils.Ataque import Ataque
from Utils.Hitbox import Hitbox
from Itens.Armas.EspadaBasica import EspadaBasica
from Personagens.Status import Status


class AbstractPersonagem(ABC):
    def __init__(self, posicao: tuple, tamanho: tuple, mapa: None) -> None:
        """Recebe um dicionário com os stats iniciais, tuplas com a posição e tamanho do personagem"""
        self.__direction = Direction.MEIO_BAIXO

        self.__arma: AbstractArma = EspadaBasica()
        self.__hitbox = Hitbox(posicao, tamanho)
        self.__mapa = mapa

    def _set_status(self, stats: dict) -> None:
        self.__status = Status(stats)

    @property
    def direction(self) -> Direction:
        return self.__direction

    @direction.setter
    def direction(self, value) -> Direction:
        if type(value) == Direction:
            self.__direction = value

    def _atualizar_frente(self, x_movement: int, y_movement: int) -> None:
        if x_movement < 0:
            if y_movement < 0:
                self.__direction = Direction.ESQUERDA_CIMA
            elif y_movement > 0:
                self.__direction = Direction.ESQUERDA_BAIXO
            else:
                self.__direction = Direction.ESQUERDA_MEIO
        elif x_movement > 0:
            if y_movement < 0:
                self.__direction = Direction.DIREITA_CIMA
            elif y_movement > 0:
                self.__direction = Direction.DIREITA_BAIXO
            else:
                self.__direction = Direction.DIREITA_MEIO
        elif y_movement > 0:
            self.__direction = Direction.MEIO_BAIXO
        elif y_movement < 0:
            self.__direction = Direction.MEIO_CIMA

    @abstractmethod
    def pontos_para_ataque(self) -> list:
        if self.__direction == Direction.DIREITA_BAIXO:
            return [self.hitbox.bottomright, self.hitbox.midrightbottom, self.hitbox.midbottomright]
        elif self.__direction == Direction.DIREITA_MEIO:
            return [self.hitbox.midright, self.hitbox.midtopright, self.hitbox.midbottomright]
        elif self.__direction == Direction.DIREITA_CIMA:
            return [self.hitbox.midright, self.hitbox.midrighttop, self.hitbox.midtopright]
        elif self.__direction == Direction.ESQUERDA_BAIXO:
            return [self.hitbox.bottomleft, self.hitbox.midbottomleft, self.hitbox.midleftbottom]
        elif self.__direction == Direction.ESQUERDA_MEIO:
            return [self.hitbox.midleft, self.hitbox.midbottomleft, self.hitbox.midtopleft]
        elif self.__direction == Direction.ESQUERDA_CIMA:
            return [self.hitbox.topleft, self.hitbox.midtopleft, self.hitbox.midlefttop]
        elif self.__direction == Direction.MEIO_BAIXO:
            return [self.hitbox.midbottom, self.hitbox.midrightbottom, self.hitbox.midleftbottom]
        elif self.__direction == Direction.MEIO_CIMA:
            return [self.hitbox.midtop, self.hitbox.midlefttop, self.hitbox.midrighttop]

    def _determinar_posicao_frente(self) -> tuple:
        if self.__direction == Direction.DIREITA_BAIXO:
            return self.hitbox.bottomright
        elif self.__direction == Direction.DIREITA_MEIO:
            return self.hitbox.midright
        elif self.__direction == Direction.DIREITA_CIMA:
            return self.hitbox.topright
        elif self.__direction == Direction.ESQUERDA_BAIXO:
            return self.hitbox.bottomleft
        elif self.__direction == Direction.ESQUERDA_MEIO:
            return self.hitbox.midleft
        elif self.__direction == Direction.ESQUERDA_CIMA:
            return self.hitbox.topleft
        elif self.__direction == Direction.MEIO_BAIXO:
            return self.hitbox.midbottom
        elif self.__direction == Direction.MEIO_CIMA:
            return self.hitbox.midtop
        else:
            return self.hitbox.midtop

    @abstractmethod
    def receber_ataque(self, ataque: Ataque) -> int:
        pass

    @abstractmethod
    def update(self):
        pass

    @property
    def alcance(self) -> int:
        return self.__arma.alcance + self.__status.alcance

    @property
    def vida_maxima(self) -> int:
        return self.__status.vida_maxima

    @vida_maxima.setter
    def vida_maxima(self, value: int) -> None:
        self.__status.vida_maxima = value

    @property
    def vida(self) -> int:
        return self.__status.vida

    @vida.setter
    def vida(self, value: int) -> None:
        self.__status.vida = value

    @property
    def vel(self) -> int:
        return self.__status.vel

    @vel.setter
    def vel(self, value: int) -> None:
        self.__status.vel = value

    @property
    def vel_ataque(self) -> int:
        return self.__status.vel_ataque

    @vel_ataque.setter
    def vel_ataque(self, value: int) -> None:
        self.__status.vel_ataque = value

    @property
    def dano(self) -> int:
        return self.__status.ataque + self.__arma.dano

    @property
    def invencibilidade(self) -> bool:
        return self.__status.invencibilidade

    @invencibilidade.setter
    def invencibilidade(self, value: bool) -> None:
        self.__status.invencibilidade = value

    @property
    def arma(self) -> AbstractArma:
        return self.__arma

    @arma.setter
    def arma(self, arma) -> None:
        if isinstance(arma, AbstractArma):
            self.__arma = arma

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa(self, value) -> None:
        self.__mapa = value

    @property
    def hitbox(self) -> Hitbox:
        return self.__hitbox

    def set_hitbox(self, hitbox: Hitbox) -> None:
        if isinstance(hitbox, Hitbox):
            self.__hitbox = hitbox

    @property
    def status(self) -> Status:
        return self.__status

    @status.setter
    def status(self, status: Status) -> None:
        if isinstance(status, Status):
            self.__status = status

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def animate(self) -> None:
        pass

    @property
    @abstractmethod
    def hurt_sound_path(self) -> str:
        pass

    @property
    @abstractmethod
    def dying_sound_path(self) -> str:
        pass

    @property
    @abstractmethod
    def morreu(self) -> bool:
        pass

    @property
    @abstractmethod
    def morrendo(self) -> bool:
        pass

    @property
    @abstractmethod
    def image(self) -> Surface:
        pass

    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass
