from Screen.States.AbstractState import AbstractState
from Screen.Views.PlayGameView import PlayGameView
from Config.Enums import States


class PlayGameState(AbstractState):
    __STATE = States.PLAY

    def __init__(self) -> None:
        view = PlayGameView()
        super().__init__(view, PlayGameState.__STATE)
