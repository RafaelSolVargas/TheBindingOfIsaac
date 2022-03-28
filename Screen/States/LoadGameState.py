from Screen.States.AbstractState import AbstractState
from Screen.Views.LoadGameView import LoadGameView
from Config.Enums import States


class LoadGameState(AbstractState):
    __STATE = States.LOAD

    def __init__(self) -> None:
        view = LoadGameView()
        super().__init__(view, LoadGameState.__STATE)
