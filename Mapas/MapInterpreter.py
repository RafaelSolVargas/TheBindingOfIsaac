from random import choice, shuffle


class MapInterpreter:
    def __init__(self, matrix: list) -> None:
        self.__input_matrix = matrix.copy()
        self.__obstacles_char = ['P', '0', '1', '2']
        self.__block_movement_and_vision_char = 'P'
        self.__block_only_movement_char = '0'
        self.__block_only_vision_char = '1'
        self.__non_block_char = '2'
        self.__end_map_char = 'E'
        self.__init_map_char = 'I'
        self.__player_start_char = 'J'
        self.__player_return_char = 'R'

        self.__matrix = self.__get_matrix_with_only_obstacles(matrix)
        self.__start_player_position = self.__get_start_player_position()
        self.__return_player_position = self.__get_return_player_position()
        self.__enemies_start_position = self.__get_all_enemies_position()
        shuffle(self.__enemies_start_position)

        self.__set_init_and_end_map_positions()
        self.__set_all_positions_blocking()

    def get_matrix_only_obstacles(self) -> list:
        return self.__matrix.copy()

    @property
    def player_start_position(self) -> tuple:
        return self.__start_player_position

    @property
    def player_return_position(self) -> tuple:
        return self.__return_player_position

    def get_random_enemy_position(self) -> tuple:
        return choice(self.__enemies_start_position)

    def get_enemies_positions(self) -> list:
        return self.__enemies_start_position

    @property
    def positions_blocking_movement_and_vision(self) -> list:
        return self.__positions_blocking_vision_and_movement

    @property
    def positions_blocking_only_movement(self) -> list:
        return self.__positions_blocking_only_movement

    @property
    def positions_blocking_only_vision(self) -> list:
        return self.__positions_blocking_only_vision

    @property
    def positions_blocking_nothing(self) -> list:
        return self.__positions_blocking_nothing

    @property
    def positions_blocking_movement(self) -> list:
        return self.__position_blocking_movement

    @property
    def positions_blocking_vision(self) -> list:
        return self.__position_blocking_vision

    @property
    def end_map_positions(self) -> list:
        return self.__end_map_positions

    @property
    def init_map_positions(self) -> list:
        return self.__init_map_positions

    def is_position_valid(self, posicao: tuple) -> bool:
        x = int(posicao[0])
        y = int(posicao[1])

        if x < 0 or x >= len(self.__matrix):
            print(f'Acesso indevido a matriz em [{x}][{y}] - 3')
            return False

        if y < 0 or y >= len(self.__matrix[0]):
            print(f'Acesso indevido a matriz em [{x}][{y}] - 4')
            return False

        return True

    def __set_all_positions_blocking(self) -> None:
        positions_blocking_both = []
        positions_blocking_vision = []
        positions_blocking_movement = []
        positions_blocking_nothing = []

        for pos_y, linha in enumerate(self.__input_matrix):
            for pos_x, cell in enumerate(linha):
                position = (pos_y, pos_x)

                if cell == self.__block_movement_and_vision_char:
                    positions_blocking_both.append(position)
                elif cell == self.__block_only_movement_char:
                    positions_blocking_movement.append(position)
                elif cell == self.__block_only_vision_char:
                    positions_blocking_vision.append(position)
                elif cell == self.__non_block_char:
                    positions_blocking_nothing.append(position)

        self.__positions_blocking_vision_and_movement = positions_blocking_both
        self.__positions_blocking_only_movement = positions_blocking_movement
        self.__positions_blocking_only_vision = positions_blocking_vision
        self.__positions_blocking_nothing = positions_blocking_nothing

        self.__position_blocking_movement = positions_blocking_movement
        self.__position_blocking_movement.extend(positions_blocking_both)

        self.__position_blocking_vision = positions_blocking_vision
        self.__position_blocking_vision.extend(positions_blocking_both)

    def __set_init_and_end_map_positions(self):
        init_positions = []
        end_positions = []

        for pos_x, linha in enumerate(self.__input_matrix):
            for pos_y, cell in enumerate(linha):
                if cell == self.__end_map_char:
                    end_positions.append((pos_x, pos_y))
                elif cell == self.__init_map_char:

                    init_positions.append((pos_x, pos_y))

        self.__end_map_positions = end_positions
        self.__init_map_positions = init_positions

    def __get_matrix_with_only_obstacles(self, matrix_input: list) -> list:
        matrix = matrix_input.copy()

        for pos_x, linha in enumerate(matrix):
            for pos_y, cell in enumerate(linha):
                if cell not in self.__obstacles_char and cell != ' ':
                    linha = self.__trocar_char_in_string(linha, pos_y, ' ')
            matrix[pos_x] = linha

        return matrix

    def __get_all_enemies_position(self) -> list:
        enemies_positions = []

        for pos_x, linha in enumerate(self.__input_matrix):
            for pos_y, cell in enumerate(linha):
                if cell == '5':
                    position = (pos_x, pos_y)
                    enemies_positions.append(position)

        return enemies_positions

    def __get_start_player_position(self) -> tuple:
        for pos_x, linha in enumerate(self.__input_matrix):
            for pos_y, cell in enumerate(linha):
                if cell == self.__player_start_char:
                    position = (pos_x, pos_y)
                    return position

    def __get_return_player_position(self) -> tuple:
        for pos_x, linha in enumerate(self.__input_matrix):
            for pos_y, cell in enumerate(linha):
                if cell == self.__player_return_char:
                    position = (pos_x, pos_y)
                    return position

    def __trocar_char_in_string(self, string_input: str, pos: int, new_char: str) -> str:
        antes = string_input[0:pos]
        depois = string_input[pos+1:]
        return f'{antes}{new_char}{depois}'
