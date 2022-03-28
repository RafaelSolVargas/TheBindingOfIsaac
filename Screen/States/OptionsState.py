from Screen.States.AbstractState import AbstractState
from Screen.Views.OptionsView import OptionsView
from Config.Enums import States


class OptionsState(AbstractState):
    __STATE = States.OPTIONS

    def __init__(self) -> None:
        view = OptionsView()
        super().__init__(view, OptionsState.__STATE)
