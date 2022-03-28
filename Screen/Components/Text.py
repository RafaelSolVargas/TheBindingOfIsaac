import pygame
from Config.Enums import Dificuldade
from Config.Opcoes import Opcoes
from Utils.Hitbox import Hitbox


class Text:
    def __init__(self, posicao: tuple, text_size: int, texto: str) -> None:
        self.__input_text = texto
        self.__font = pygame.font.SysFont('Agency FB', text_size)
        self.__color = (255, 50, 50)

        self.__text = self.__font.render(self.__input_text, True, self.__color)
        self.__text_rect = self.__text.get_rect(center=posicao)

    def desenhar(self, tela):
        # pygame.draw.rect(tela.janela, (0, 0, 0), self.__text_rect)
        tela.janela.blit(self.__text, self.__text_rect)

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, texto):
        if type(texto) == str:
            self.__input_text = texto
            self.__text = self.__font.render(self.__input_text, True, self.__color)

    @property
    def hitbox(self) -> Hitbox:
        return self.__hitbox


class DifficultyText(Text):
    def __init__(self, posicao: tuple, text_size: int) -> None:
        self.__opcoes = Opcoes()
        text = self.__get_updated_text()
        super().__init__(posicao, text_size, text)

    def desenhar(self, tela):
        self.text = self.__get_updated_text()
        return super().desenhar(tela)

    def __get_updated_text(self) -> str:
        difficulty = 'Easy'
        if self.__opcoes.dificuldade == Dificuldade.medio:
            difficulty = 'Normal'
        elif self.__opcoes.dificuldade == Dificuldade.dificil:
            difficulty = 'Hard'

        return f'Difficulty: {difficulty}'
