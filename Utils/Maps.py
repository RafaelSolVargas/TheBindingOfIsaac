class MapUpdater:
    def __init__(self, matrix: list) -> None:
        self.__matrix = matrix
        self.__invalid_char = 'X'
        self.__valid_chars = [' ']
        self.__not_updated_invalid_chars = ['P', '0', '1', '2']
        self.__points_blocking_movement = ['P', '0']

    def update_map_for_size(self, size) -> list:
        matrix = self.__matrix.copy()

        x_proporsion = size[0]
        y_proporsion = size[1]
        diagonal_proporsion = min(x_proporsion, y_proporsion)

        for x, linha in enumerate(matrix):
            for y, ponto in enumerate(linha):
                lateral_points = []
                lateral_points.extend(
                    self.__get_lateral_points_x_with_proporsion((x, y), x_proporsion))
                lateral_points.extend(
                    self.__get_lateral_points_y_with_proporsion((x, y), y_proporsion))
                lateral_points.extend(
                    self.__get_lateral_points_diagonal_with_proporsion((x, y), diagonal_proporsion))

                for ponto_lateral in lateral_points:
                    if self.__ponto_ocupado(ponto_lateral):
                        if ponto not in self.__not_updated_invalid_chars:

                            matrix[x] = self.__trocar_char_in_string(matrix[x], y)

                            break

        return matrix

    def validate_ponto_in_matrix(self, ponto: tuple, matrix: list) -> bool:
        x = int(ponto[0])
        y = int(ponto[1])

        if x < 0 or x >= len(matrix):
            print(f'Acesso indevido a matriz em [{x}][{y}] - 1')
            return False

        if y < 0 or y >= len(matrix[0]):
            print(f'Acesso indevido a matriz em [{x}][{y}] - 2')
            return False

        if matrix[x][y] not in self.__valid_chars:
            return False

        return True

    def __ponto_ocupado(self, ponto: tuple):
        x = int(ponto[0])
        y = int(ponto[1])

        if x < 0 or x >= len(self.__matrix):
            return False

        if y < 0 or y >= len(self.__matrix[0]):
            return False

        if self.__matrix[x][y] not in self.__points_blocking_movement:
            return False

        if self.__matrix[x][y] in self.__valid_chars:
            return False

        return True

    def __get_lateral_points_x_with_proporsion(self, ponto: tuple, proporsion: int) -> list:
        pontos_laterais = []
        for x in range(1, proporsion):
            pontos_laterais.append((ponto[0] + x, ponto[1]))

        return pontos_laterais

    def __get_lateral_points_y_with_proporsion(self, ponto: tuple, proporsion: int) -> list:
        pontos_laterais = []
        for y in range(1, proporsion):
            pontos_laterais.append((ponto[0], ponto[1] + y))

        return pontos_laterais

    def __get_lateral_points_diagonal_with_proporsion(self, ponto: tuple, proporsion: int) -> list:
        pontos_laterais = []
        for x in range(1, proporsion):
            for y in range(1, proporsion):
                pontos_laterais.append((ponto[0] + x, ponto[1] + y))

        return pontos_laterais

    def __trocar_char_in_string(self, string_input: str, pos: int) -> str:
        antes = string_input[0:pos]
        depois = string_input[pos+1:]
        return f'{antes}{self.__invalid_char}{depois}'
