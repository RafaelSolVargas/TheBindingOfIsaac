from abc import abstractmethod
from typing import Dict, List
from Config.Opcoes import Opcoes
from Config.Enums import Direction
from Personagens.AbstractInimigo import AbstractInimigo
from Mapas.AbstractMapa import AbstractMapa
from Utils.Converter import Converter
from Utils.Folder import import_fliped_folder, import_folder
from Utils.Hitbox import Hitbox
from random import random
from pygame import Surface, Rect


class InimigoTipo1(AbstractInimigo):
    __PATH_TO_SPRITES = {}

    def __init__(self, mapa: AbstractMapa, path: str, posicao=(0, 0)) -> None:
        super().__init__(posicao=posicao, mapa=mapa)
        stats = self.__calibrar_dificuldade()
        super()._set_status(stats)

        if path not in self.__PATH_TO_SPRITES:
            sprites = self.__import_character_assets()
            self.__PATH_TO_SPRITES[path] = sprites
        else:
            sprites = InimigoTipo1.__PATH_TO_SPRITES[path]

        self._normal_animations = self.__PATH_TO_SPRITES[path][0]
        self._fliped_animations = self.__PATH_TO_SPRITES[path][1]
        self._animations_length = self.__PATH_TO_SPRITES[path][2]
        self._animations = self._normal_animations

        self.__animation = 'Idle'
        self.__frame_index = 0
        self.__animation_speed = 0.35
        self.__FRAME_TO_WAIT = 0
        self.__MORREU = False
        self.__LAST_ANIMATION = 'Idle'
        self.__ANIMACAO_RESETADA = False
        self.__MAX_DELAY_ATAQUE = Converter.vel_ataque_to_delay(self.vel_ataque)
        self.__CURRENT_DELAY_ATAQUE = 0

    def __import_character_assets(self) -> List[Dict]:
        animations_length = {}
        normal_animations = {}
        fliped_animations = {}

        animations_names = ['Idle', 'Walking', 'Taunt', 'Idle Blink',
                            'Attacking', 'Dying', 'Hurt']

        for animation in animations_names:
            full_path = self._SPRITE_PATH + animation

            normal_images = import_folder(full_path, self._TAMANHO_IMAGEM)
            fliped_images = import_fliped_folder(full_path, self._TAMANHO_IMAGEM)

            fliped_animations[animation] = fliped_images
            normal_animations[animation] = normal_images
            animations_length[animation] = len(normal_images)

        return [normal_animations, fliped_animations, animations_length]

    def __calibrar_dificuldade(self) -> dict:
        dificuldade = Opcoes().dificuldade
        if dificuldade.medio:
            return self._STATS_MEDIO
        elif dificuldade.dificil:
            return self._STATS_DIFICIL
        else:
            return self._STATS_FACIL

    @property
    def image(self) -> Surface:
        if self.__frame_index >= len(self._animations[self.__animation]):
            self.__frame_index = 0

        self.__image = self._animations[self.__animation][int(self.__frame_index)]
        return self.__image

    @property
    def rect(self) -> Rect:
        self.__rect = self.__image.get_rect(center=self.hitbox.center)
        return self.__rect

    @rect.setter
    def rect(self, value: Rect) -> None:
        if type(value) == Rect:
            self.__rect = value

    def animate(self) -> None:
        animation_name = self.__get_current_animation()
        animation = self._animations[animation_name]

        if self.__ANIMACAO_RESETADA:
            self.__ANIMACAO_RESETADA = False

        # Reseta o frame index caso tenha trocado a animação
        if self.__LAST_ANIMATION != animation_name:
            self.__frame_index = 0
        self.__LAST_ANIMATION = animation_name

        self.__frame_index += self.__animation_speed
        if self.__frame_index >= len(animation):
            self.__frame_index = 0
            self.__ANIMACAO_RESETADA = True

    def mover(self, *args) -> None:
        # Se está atacando ou tomou dano não vai andar até a animação terminar
        if self.__animation == 'Attacking' or self.__animation == 'Hurt':
            if self.__FRAME_TO_WAIT > 0:
                return None

        return super().mover(*args)

    def atacar(self) -> bool:
        # Caso tenha morrido ou tomado dano, não vai atacar
        if self.__MORREU or self.__animation == 'Hurt':
            return False

        if self.__animation == 'Attacking':
            if self.__FRAME_TO_WAIT == self._FRAME_EXECUTAR_ATAQUE:
                return True
            else:
                return False

        return False

    def update(self, hit_jogador: Hitbox) -> None:
        distancia = self._calcular_distancia(hit_jogador)

        if self.__CURRENT_DELAY_ATAQUE > 0:
            self.__CURRENT_DELAY_ATAQUE -= 1

        # Update de qual a fonte de sprite, esquerda ou direita
        if self.direction == Direction.DIREITA_BAIXO or self.direction == Direction.DIREITA_CIMA or self.direction == Direction.DIREITA_MEIO:
            self._animations = self._normal_animations
        else:
            self._animations = self._fliped_animations

        # Update quanto a animação de atacar
        if self.__animation != 'Attacking' and self.__animation != 'Hurt':
            # Se não está atacando e não tomou hit
            if distancia < self._DIST_PARA_ATAQUE:  # Se está perto troca animação para atacar
                if self.__CURRENT_DELAY_ATAQUE == 0:
                    self.__set_animation('Attacking')
                    self.__CURRENT_DELAY_ATAQUE = self.__MAX_DELAY_ATAQUE
                else:
                    self.__set_animation('Idle')

        # Update para cancelar ataque caso jogador saia do range ou caso tome hit
        if self.__animation == 'Attacking':
            if self._tomou_dano():
                if self.__will_damage_stop_attack():
                    self.__set_animation('Hurt')
            elif distancia > self.alcance + 10:
                self.__set_animation('Walking')

        return super().update(hit_jogador)

    @property
    def morreu(self) -> bool:
        if self.vida <= 0:
            if not self.__MORREU:
                self.hitbox.transpassavel = True
                self.__set_animation('Dying')
            else:
                if self.__ANIMACAO_RESETADA:
                    return True
                else:
                    return False
        return False

    def __get_current_animation(self) -> str:
        if self.__FRAME_TO_WAIT > 0:
            self.__FRAME_TO_WAIT -= 1
            return self.__animation

        if self._state.REPOUSO:
            self.__set_animation('Repouso')
        elif self._state.MORRENDO:
            self.__set_animation('Dying')
        elif self._state.ALERTA:
            self.__set_animation('Procurando')
        elif self._tomou_dano():
            self.__set_animation('Hurt')
        elif self._state.ATACANDO:
            self.__set_animation('Walking')

        return self.__animation

    def __set_animation(self, animation: str) -> None:
        # Animação não pode ser sobreposta
        if self.__animation == 'Dying':
            return None
        self.__FRAME_TO_WAIT = 0

        if animation == 'Attacking':
            self.__animation = animation
            self.__set_animation_frame_to_wait(animation)

        if animation == 'Dying':
            self.__MORREU = True
            self.__animation = animation
            self.__set_animation_frame_to_wait(animation)

        if animation == 'Hurt':
            self.__animation = animation
            self.__set_animation_frame_to_wait(animation)

        if animation == 'Walking':
            self.__animation = animation

        if animation == 'Repouso':
            if self.__ANIMACAO_RESETADA:
                self.__animation = self.__get_random_idle_animation()

        if animation == 'Procurando':
            if self.__ANIMACAO_RESETADA:
                self.__animation = self.__get_random_searching_animation()

    def __set_animation_frame_to_wait(self, animation: str) -> None:
        self.__FRAME_TO_WAIT = self._animations_length[animation] // self.__animation_speed

    def __will_damage_stop_attack(self) -> bool:
        chance = random()

        if chance < self._CHANCE_DAMAGE_STOP_ATTACK:
            return True
        else:
            return False

    def __get_random_idle_animation(self) -> str:
        if 0.1 > random():
            return 'Taunt'
        if 0.3 > random():
            return 'Idle Blink'
        else:
            return 'Idle'

    def __get_random_searching_animation(self) -> str:
        if 0.15 > random():
            return 'Taunt'
        else:
            return 'Walking'

    @property
    @abstractmethod
    def _STATS_DIFICIL(self) -> dict:
        pass

    @property
    @abstractmethod
    def _STATS_MEDIO(self) -> dict:
        pass

    @property
    @abstractmethod
    def _STATS_FACIL(self) -> dict:
        pass

    @property
    @abstractmethod
    def _SPRITE_PATH(self) -> str:
        pass

    @property
    @abstractmethod
    def _TAMANHO(self) -> tuple:
        pass

    @property
    @abstractmethod
    def _CHANCE_DAMAGE_STOP_ATTACK(self) -> float:
        pass

    @property
    @abstractmethod
    def _TAMANHO_IMAGEM(self) -> tuple:
        pass

    @property
    @abstractmethod
    def _DIST_PARA_ATAQUE(self) -> tuple:
        pass

    @property
    @abstractmethod
    def _FRAME_EXECUTAR_ATAQUE(self) -> int:
        pass

    @property
    def morrendo(self) -> bool:
        if self.__animation == 'Dying':
            return True
        else:
            return False
