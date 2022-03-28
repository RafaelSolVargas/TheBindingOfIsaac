from typing_extensions import Self
from Config.Enums import Estado
from Personagens.AbstractPersonagem import AbstractPersonagem
from Personagens.AbstractSignal import AbstractSignal
from Utils.Hitbox import Hitbox


class EnemyState(AbstractSignal):
    __RANGE = 145

    def __init__(self, state: Estado, hitbox: Hitbox, sender: AbstractPersonagem) -> None:
        self.__state = state
        self.__hitbox = hitbox
        self.__sender = sender

    def update_state(self, ally_state: Self) -> Estado:
        if ally_state.MORRENDO:
            return ally_state

        if self.__state.ATACANDO:
            if ally_state != Estado.ATACANDO:
                ally_state.state = Estado.ATACANDO

        elif self.__state.ALERTA:
            if ally_state.REPOUSO:
                ally_state.state = Estado.ALERTA

        return ally_state

    @property
    def sender(self) -> AbstractPersonagem:
        return self.__sender

    @property
    def source_position(self) -> tuple:
        return self.__hitbox.center

    @property
    def signal_range(self) -> int:
        return EnemyState.__RANGE

    @property
    def state(self) -> Estado:
        return self.__state

    @state.setter
    def state(self, new_state) -> None:
        if type(new_state) == Estado:
            self.__state = new_state

    @property
    def MORRENDO(self) -> bool:
        if self.__state == Estado.MORRENDO:
            return True
        else:
            return False

    @property
    def REPOUSO(self) -> bool:
        if self.__state == Estado.REPOUSO:
            return True
        else:
            return False

    @property
    def ALERTA(self) -> bool:
        if self.__state == Estado.ALERTA:
            return True
        else:
            return False

    @property
    def ATACANDO(self) -> bool:
        if self.__state == Estado.ATACANDO:
            return True
        else:
            return False
