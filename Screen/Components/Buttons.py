from abc import ABC, abstractmethod
from typing import Any, List
from Config.Folder import Folder
from Config.Opcoes import Opcoes
from Config.Enums import Dificuldade, States
from Jogo.ControllerJogo import ControllerJogo
from Sounds.MusicHandler import MusicHandler
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from pygame import K_BACKSPACE, KEYDOWN, MOUSEBUTTONDOWN, Rect, draw, font, MOUSEBUTTONUP
from pygame.event import Event
import pygame


class Button(ABC):
    def __init__(self, position, size, next_state: States) -> None:
        self.__position = position
        self.__size = size
        self.__next_state = next_state

        self.__hover_color = (255, 50, 50)
        self.__normal_color = (200, 125, 125)

        self.__rect = Rect(self.__position, self.__size)
        self.__color = self.__normal_color
        self.__clicked = False

    def run(self, events: List[Event]) -> None:
        self.__clicked = False

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            for event in events:
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    self.__clicked = True

    @property
    def clicked(self) -> bool:
        return self.__clicked

    def hover(self) -> None:
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            self.__color = self.__hover_color
        else:
            self.__color = self.__normal_color

    @property
    def rect(self) -> Rect:
        return self.__rect

    @property
    def color(self) -> tuple:
        return self.__color

    @color.setter
    def color(self, value: tuple) -> None:
        self.__color = value

    @property
    def next_state(self) -> Any:
        return self.__next_state

    @abstractmethod
    def desenhar(self, tela: TelaJogo) -> None:
        draw.rect(tela.janela, self.__color, self.__rect, 3, 8)

    @property
    def position(self) -> tuple:
        return self.__position

    @abstractmethod
    def get_state(self) -> States:
        pass


class TextButton(Button):
    def __init__(self, text, position, size, next_state: States) -> None:
        rect = Rect(position, size)
        rect.center = rect.topleft
        position = rect.topleft

        super().__init__(position, size, next_state)
        self.__color = (255, 255, 255)
        self.__font = font.SysFont('Agency FB', 25)
        self.__text = text
        self.__text_surf = self.__font.render(text, True, self.__color)
        self.__text_rect = self.__text_surf.get_rect(center=self.rect.center)

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value) -> None:
        if type(value) == str:
            self.__text = value
            self.__text_surf = self.__font.render(self.__text, True, self.__color)
            self.__text_rect = self.__text_surf.get_rect(center=self.rect.center)

    def desenhar(self, tela: TelaJogo) -> None:
        super().desenhar(tela)
        tela.janela.blit(self.__text_surf, self.__text_rect)

    def get_state(self) -> States:
        if self.clicked:
            return self.next_state
        else:
            return States.SAME


class ImageButton(Button):
    def __init__(self, position, size, path, scale, next_state: States) -> None:
        super().__init__(position, size, next_state)
        self.__scale = scale
        self.__image = import_single_sprite(path, (60, 60))
        self.__rect = self.__image.get_rect(topleft=position)
        self.__path_to_sprite = {path: self.__image}

    def desenhar(self, tela: TelaJogo) -> None:
        tela.janela.blit(self.__image, self.__rect)

    def _change_path(self, path: str) -> None:
        if path in self.__path_to_sprite.keys():
            self.__image = self.__path_to_sprite[path]
            self.__rect = self.__image.get_rect(topleft=self.position)
        else:
            self.__image = import_single_sprite(path, self.__scale)
            self.__rect = self.__image.get_rect(topleft=self.position)
            self.__path_to_sprite[path] = self.__image

    def get_state(self) -> States:
        if self.clicked:
            return self.next_state
        else:
            return States.SAME


class MenuButton(TextButton):
    __SIZE = (130, 45)

    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, MenuButton.__SIZE, next_state)


class SaveNameButton(MenuButton):
    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, next_state)
        self.__active = False
        self.__rect_active_color = (255, 50, 50)

    def run(self, events: List[Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.__active = True
                else:
                    self.__active = False

    def desenhar(self, tela: TelaJogo) -> None:
        if self.__active:
            self.color = self.__rect_active_color
        else:
            self.hover()

        super().desenhar(tela)

    @property
    def active(self) -> bool:
        return self.__active


class SaveButton(MenuButton):
    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, next_state)
        self.__dao = ControllerJogo()

    def run(self, events: List[Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.__executar()
        super().run(events)

    def __executar(self) -> None:
        self.__dao.save()

    @property
    def active(self) -> bool:
        return self.__active


class ImageTextButton(ImageButton):
    def __init__(self, position, size, path, scale, next_state: States) -> None:
        folder = Folder()
        path = folder.create_assets_path(['Telas'], 'botao.png')
        scale = (100, 35)
        super().__init__(position, size, path, scale, next_state)
        TextButton.__init__(self, 'Test', position, size, next_state)

    def desenhar(self, tela: TelaJogo) -> None:
        ImageButton.desenhar(tela)


class MusicButton(TextButton):
    __SIZE = (130, 45)

    def __init__(self, position, next_state: States) -> None:
        self.__music = MusicHandler()
        self.__opcoes = Opcoes()
        text = self.__get_current_music_status_text()
        super().__init__(text, position, MusicButton.__SIZE, next_state)

    def get_state(self) -> States:
        if self.clicked:
            self.__executar()
            return self.next_state
        else:
            return States.SAME

    def __get_current_music_status_text(self) -> str:
        if self.__music.playing:
            return 'Music: On'
        else:
            return 'Music: Off'

    def __executar(self) -> None:
        self.__music.toggle_pause()
        self.__opcoes.tocar_musica = not self.__opcoes.tocar_musica

    def __update(self) -> None:
        self.text = self.__get_current_music_status_text()

    def desenhar(self, tela: TelaJogo) -> None:
        self.__update()
        super().desenhar(tela)


class MusicImageButton(ImageButton):
    folder = Folder()
    __MUTED_PATH = folder.create_assets_path(['Telas'], 'mutado.png')
    __NOT_MUTED_PATH = folder.create_assets_path(['Telas'], 'som.png')

    def __init__(self, position, size, scale, next_state: States) -> None:
        self.__music = MusicHandler()
        self.__opcoes = Opcoes()

        path = self.__get_current_path()
        super().__init__(position, size, path, scale, next_state)

    def __get_current_path(self) -> str:
        if self.__opcoes.tocar_musica:
            return MusicImageButton.__NOT_MUTED_PATH
        else:
            return MusicImageButton.__MUTED_PATH

    def get_state(self) -> States:
        if self.clicked:
            self.__executar()
            return self.next_state
        else:
            return States.SAME

    def run(self, events: List[Event]) -> None:
        return super().run(events)

    def __executar(self) -> None:
        self.__opcoes.tocar_musica = not self.__opcoes.tocar_musica
        self.__music.toggle_pause()
        path = self.__get_current_path()
        super()._change_path(path)

    def desenhar(self, tela: TelaJogo) -> None:
        path = self.__get_current_path()
        super()._change_path(path)
        super().desenhar(tela)


class ButtonDificil(MenuButton):
    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, next_state)

    def get_state(self) -> States:
        if self.clicked:
            self.__executar()
            return self.next_state
        else:
            return States.SAME

    def __executar(self) -> None:
        self.__opcoes = Opcoes()
        self.__opcoes.dificuldade = Dificuldade.dificil


class ButtonMedio(MenuButton):
    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, next_state)

    def get_state(self) -> States:
        if self.clicked:
            self.__executar()
            return self.next_state
        else:
            return States.SAME

    def __executar(self) -> None:
        self.__opcoes = Opcoes()
        self.__opcoes.dificuldade = Dificuldade.medio


class ButtonFacil(MenuButton):
    def __init__(self, text, position, next_state: States) -> None:
        super().__init__(text, position, next_state)

    def get_state(self) -> States:
        if self.clicked:
            self.__executar()
            return self.next_state
        else:
            return States.SAME

    def __executar(self) -> None:
        self.__opcoes = Opcoes()
        self.__opcoes.dificuldade = Dificuldade.facil


class InputText(TextButton):
    __SIZE = (105, 35)
    __MAX_SIZE = 10

    def __init__(self, position: tuple, default_text: str) -> None:
        super().__init__(default_text, position, InputText.__SIZE, States.SAME)

        self.__jogoOptions = ControllerJogo()
        self.__rect_active_color = (255, 50, 50)
        self.__active = False

    def desenhar(self, tela: TelaJogo) -> None:
        if self.__active:
            self.color = self.__rect_active_color
        else:
            self.hover()

        super().desenhar(tela)

    def run(self, events: List[Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.__active = True
                else:
                    self.__active = False
            if event.type == KEYDOWN:
                if self.__active:
                    if event.key == K_BACKSPACE:
                        self.__change_text(f'{self.text[:-1]}')
                    else:
                        self.__change_text(f'{self.text}{event.unicode}')

    def __change_text(self, value) -> None:
        if len(value) > InputText.__MAX_SIZE:
            return
        elif type(value) == str:
            self.text = value
            self.__jogoOptions.new_game_name = value
