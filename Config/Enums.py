from enum import Enum


class ComandosEnum(Enum):
    SAIR = 1
    VOLTAR = 2
    LOAD_GAME = 3
    NEW_GAME = 4
    TELA_OPCOES = 5
    TELA_SAVES = 6
    TELA_NEW_GAME = 7
    TELA_MENU = 8
    TELA_JOGAR = 9
    SET_DIFICULDADE = 10
    TOGGLE_MUSICA = 11


class Dificuldade(Enum):
    facil = 1
    medio = 2
    dificil = 3


class Direction(Enum):
    ESQUERDA_BAIXO = 1
    ESQUERDA_MEIO = 2
    ESQUERDA_CIMA = 3
    MEIO_CIMA = 4
    MEIO_BAIXO = 5
    DIREITA_BAIXO = 6
    DIREITA_MEIO = 7
    DIREITA_CIMA = 8


class Estado(Enum):
    ALERTA = 1
    REPOUSO = 2
    ATACANDO = 3
    MORRENDO = 4


class States(Enum):
    MENU = 1
    OPTIONS = 2
    PLAY = 3
    NEW = 4
    LOAD = 5
    SAME = 6
    QUIT = 7
    PLAYING = 8
    LOAD_GAME = 9
    CREATE_NEW = 10
    STATIC = 11
    WINNER = 12
    LOSER = 13
    RESET = 14
    GUIDE = 15
