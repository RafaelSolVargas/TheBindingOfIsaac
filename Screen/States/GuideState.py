from Screen.States.AbstractState import AbstractState
from Screen.Views.GuideView import GuideView
from Config.Enums import States


class GuideState(AbstractState):
    __STATE = States.GUIDE

    def __init__(self) -> None:
        view = GuideView()
        super().__init__(view, GuideState.__STATE)
