from Screen.States.AbstractState import AbstractState
from Screen.Views.NewGameView import NewGameView
from Config.Enums import States


class NewGameState(AbstractState):
    __STATE = States.NEW

    def __init__(self) -> None:
        view = NewGameView()
        super().__init__(view, NewGameState.__STATE)
