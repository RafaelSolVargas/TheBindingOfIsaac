from os import walk
import pygame


def import_folder(path: str, size: tuple) -> list:
    try:
        surface_list = []
        for _, _, image_files in walk(path):
            for image_name in image_files:
                full_path = f'{path}/{image_name}'
                image_surf = pygame.image.load(full_path).convert_alpha()
                image_surf = pygame.transform.scale(image_surf, size)

                surface_list.append(image_surf)

        return surface_list
    except Exception as e:
        print(f'Erro carregando sprite: {e}')
        return []


def import_fliped_folder(path: str, size: tuple) -> list:
    try:
        surface_list = []
        for _, _, image_files in walk(path):
            for image_name in image_files:
                full_path = f'{path}/{image_name}'
                image_surf = pygame.image.load(full_path).convert_alpha()
                image_surf = pygame.transform.flip(image_surf, True, False)
                image_surf = pygame.transform.scale(image_surf, size)

                surface_list.append(image_surf)

        return surface_list
    except Exception as e:
        print(f'Erro carregando sprite: {e}')
        return []


def import_single_sprite(path, size, rotate_angle=0) -> pygame.Surface:
    try:
        image_surf = pygame.image.load(path).convert_alpha()
        image_surf = pygame.transform.scale(image_surf, size)

        if rotate_angle > 0:
            image_surf = pygame.transform.rotate(image_surf, rotate_angle)

        return image_surf
    except Exception as e:
        print(f'Erro carregando sprite: {e}')
        return None
