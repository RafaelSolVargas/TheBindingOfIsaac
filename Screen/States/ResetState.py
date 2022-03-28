from typing import List
from Screen.States.AbstractState import AbstractState
from Screen.Views.PlayingView import PlayingView
from Config.Enums import States
from Config.TelaJogo import TelaJogo
from pygame.event import Event


class ResetState(AbstractState):
    __STATE = States.RESET

    def __init__(self) -> None:
        view = PlayingView()
        super().__init__(view, ResetState.__STATE)

    def run(self, events: List[Event]) -> States:
        return States.MENU

    def desenhar(self, tela: TelaJogo) -> None:
        self.view.desenhar(tela)
