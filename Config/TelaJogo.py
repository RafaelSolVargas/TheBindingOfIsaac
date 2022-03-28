import pygame
from Config.Folder import Folder
from Config.Opcoes import Opcoes


class TelaJogo():
    folder = Folder()
    __BACKGROUND_PATH = folder.create_assets_path(['Telas'], '3.jpg')

    def __init__(self) -> None:
        opcoes = Opcoes()
        self.__tamanho = opcoes.TAMANHO_TELA
        self.__janela = pygame.display.set_mode(self.__tamanho)

        imagem_fundo = pygame.image.load(TelaJogo.__BACKGROUND_PATH)
        self.__plano_fundo = pygame.transform.scale(imagem_fundo, self.__tamanho)

        pygame.display.set_caption(opcoes.GAME_TITLE)

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho) -> tuple:
        if type(tamanho) == tuple:
            self.__tamanho = tamanho

    @property
    def janela(self) -> pygame.surface:
        return self.__janela

    def mostrar_fundo(self) -> None:
        return self.__janela.blit(self.__plano_fundo, (0, 0))
