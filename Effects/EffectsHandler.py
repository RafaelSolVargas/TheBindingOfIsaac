from typing import List
from Config.TelaJogo import TelaJogo
from Effects.AbstractEffect import AbstractEffect


class EffectsHandler:
    def __init__(self) -> None:
        self.__effects: List[AbstractEffect] = []

    def desenhar(self, tela: TelaJogo):
        for effect in self.__effects:
            tela.janela.blit(effect.image, effect.rect)

    def add_effect(self, effect: AbstractEffect):
        self.__effects.append(effect)

    def update(self) -> None:
        for effect in self.__effects:
            effect.update()

            if effect.has_ended():
                self.__effects.remove(effect)
