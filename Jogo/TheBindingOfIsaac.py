from Config.Folder import Folder
from Config.TelaJogo import TelaJogo
from Sounds.MusicHandler import MusicHandler
from Screen.States.MachineState import StateMachine
import pygame


class TheBindingOfIsaac:
    folder = Folder()
    __TELAS_MUSIC_PATH = folder.create_sounds_path(['musics'], 'som_menu.mp3')

    def __init__(self) -> None:
        pygame.init()
        self.__tela = TelaJogo()
        self.__music = MusicHandler()
        self.__machine = StateMachine()
        self.__FPS = 40

    def start(self) -> None:
        self.__tela.mostrar_fundo()
        self.__music.play_music(TheBindingOfIsaac.__TELAS_MUSIC_PATH)
        self._run()

    def _run(self) -> None:
        clock = pygame.time.Clock()

        MAIN_LOOP = True
        while MAIN_LOOP:
            clock.tick(self.__FPS)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    MAIN_LOOP = False
                    pygame.quit()
                    exit()

            self.__machine.desenhar(self.__tela)
            self.__machine.run(events)
            if self.__machine.stop():
                MAIN_LOOP = False
                pygame.quit()
                exit()

            pygame.display.update()
