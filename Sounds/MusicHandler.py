from pygame import mixer
from Config.Singleton import Singleton
from Config.Opcoes import Opcoes


class MusicHandler(Singleton):
    def __init__(self) -> None:
        if not super().created:
            mixer.pre_init(44100, 16, 2, 4096)
            mixer.init()

            self.__opcoes = Opcoes()
            self.__PLAYING_MUSIC = False
            self.__current_music_path = ''

    def play_music(self, music_path: str) -> None:
        if music_path == '':
            return

        if self.__current_music_path == music_path:
            return None

        try:
            if self.__PLAYING_MUSIC:
                mixer.music.stop()

            self.__current_music_path = music_path
            mixer.music.load(music_path)
            mixer.music.play(-1)
            self.__PLAYING_MUSIC = True
            mixer.music.set_volume(0.3)
        except Exception as e:
            print(f'Error Playing Music: {e}')

    def play_music_once(self, music_path: str) -> None:
        if music_path == '':
            return

        try:
            if self.__PLAYING_MUSIC:
                mixer.music.stop()
            self.__current_music_path = music_path
            mixer.music.load(music_path)
            mixer.music.play(1)
            mixer.music.set_volume(0.3)
            self.__PLAYING_MUSIC = True
        except Exception as e:
            print(f'Error Playing Music: {e}')

    def play_sound(self, sound_path: str) -> None:
        if sound_path == '':
            return
        if not self.__opcoes.tocar_musica:
            return
        try:
            sound = mixer.Sound(sound_path)
            sound.set_volume(0.3)
            sound.play()
        except Exception as e:
            print(f'Error Playing Music: {e}')
        pass

    def update(self) -> None:
        if not self.__opcoes.tocar_musica:
            if self.__PLAYING_MUSIC:
                mixer.music.set_volume(0)
                self.__PLAYING_MUSIC = False
        else:
            if not self.__PLAYING_MUSIC:
                mixer.music.set_volume(0.3)
                self.__PLAYING_MUSIC = True

    @property
    def playing(self) -> bool:
        return self.__PLAYING_MUSIC

    def toggle_pause(self) -> None:
        if self.__PLAYING_MUSIC:
            mixer.music.set_volume(0)
            self.__PLAYING_MUSIC = False
        else:
            mixer.music.set_volume(0.3)
            self.__PLAYING_MUSIC = True
