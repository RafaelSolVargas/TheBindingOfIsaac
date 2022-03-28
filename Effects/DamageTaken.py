from Effects.AbstractEffect import AbstractEffect
from pygame import Rect, Surface, font


class DamageTaken(AbstractEffect):
    __DURATION = 60
    __FONT = 'Agency FB'
    __TEXT_SIZE = 16
    __MOVEMENT_SPEED = -0.3

    def __init__(self, damage: int, position: tuple) -> None:
        self.__duration = DamageTaken.__DURATION
        self.__text = f'-{damage}'
        self.__position = position
        self.__float_pos = position
        self.__DONE = False

        self.__text_color = (200, 50, 50)
        self.__font = font.SysFont(DamageTaken.__FONT, DamageTaken.__TEXT_SIZE)
        self.__image = self.__font.render(self.__text, False, self.__text_color)
        self.__rect = self.__image.get_rect(center=self.__position)

    def has_ended(self) -> bool:
        return self.__DONE

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        self.__rect = self.__image.get_rect(center=self.__position)
        return self.__rect

    def update(self) -> None:
        self.__float_pos = (self.__float_pos[0], self.__float_pos[1] + DamageTaken.__MOVEMENT_SPEED)
        self.__position = (int(self.__float_pos[0]), int(self.__float_pos[1]))

        if self.__duration > 0:
            self.__duration -= 1
        else:
            self.__DONE = True
