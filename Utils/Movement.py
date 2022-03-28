from typing import List
from math import sqrt


class GAHandler:
    @classmethod
    def gerar_equação_vetorial_reta(cls, p1, p2):
        def funcao(x):
            sub = ((p2[0] - p1[0]) * x, (p2[1] - p1[1]) * x)
            ponto = (p1[0] + sub[0], p1[1] + sub[1])
            return ponto

        return funcao

    @classmethod
    def distancia_dois_pontos(cls, p1: tuple, p2: tuple) -> float:
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** (1/2)


class NodeHeap:
    def __init__(self, index, value) -> None:
        self.value: Node = value
        self.index = index

    @property
    def parent(self):
        return (self.index-1) // 2

    @property
    def left(self):
        return self.index * 2 + 1

    @property
    def right(self):
        return self.index * 2 + 2


class Node:
    def __init__(self, position: tuple, parent) -> None:
        self.parent: Node = parent
        self.position = position

        self.f = 0  # Distance
        self.g = 0  # Start-Node
        self.h = 0  # Node-End

    def __gt__(self, x) -> bool:
        if type(x) == type(self):
            if self.f == x.f:
                # Utiliza um tie breaking entregando valores mais longe do inicio
                return self.g < x.g
            else:
                return self.f > x.f
        elif type(x) == int or type(x) == float:
            return self.f > x
        else:
            print(f'Invalid Type GT: {type(self)}-{type(x)}')
            return False

    def __lt__(self, x) -> bool:
        if type(x) == type(self):
            if self.f == x.f:
                # Utiliza um tie breaking entregando valores mais longe do inicio
                return self.g > x.g
            else:
                return self.f < x.f
        elif type(x) == int or type(x) == float:
            return self.f < x
        else:
            print(f'Invalid Type LT: {type(self)}-{type(x)}')
            return False

    def __le__(self, x) -> bool:
        if type(x) == type(self):
            if self.f == x.f:
                return self.h <= x.h
            else:
                return self.f <= x.f
        elif type(x) == int or type(x) == float:
            return self.f <= x
        else:
            print(f'Invalid Type LE: {type(self)}-{type(x)}')
            return False

    def __ge__(self, x) -> bool:
        if type(x) == type(self):
            if self.f == x.f:
                return self.h >= x.h
            else:
                return self.f >= x.f
        elif type(x) == int or type(x) == float:
            return self.f >= x
        else:
            print(f'Invalid Type GE: {type(self)}-{type(x)}')
            return False

    def __eq__(self, x) -> bool:
        if type(x) == type(self):
            return self.position == x.position
        elif type(x) == tuple:
            return self.position == x
        elif x is None:
            return False
        else:
            print(f'Invalid Type EQ: {type(self)}-{type(x)}')
            return False

    def __ne__(self, x) -> bool:
        if type(x) == type(self):
            return self.position != x.position
        else:
            print(f'Invalid Type NE: {type(self)}-{type(x)}')
            return False


class MinHeap:
    def __init__(self, array: list) -> None:
        self.heap: List[NodeHeap] = array

    def printHeap(self) -> None:
        print([(node.value.f, node.value.position) for node in self.heap])

    def insert(self, value) -> None:
        newIndex = len(self.heap)
        newNode = NodeHeap(newIndex, value)
        self.heap.append(newNode)

        self.__increase_value(newNode)

    def minimun(self) -> int:
        if len(self.heap) > 0:
            return self.heap[0].value

    def popMinimum(self) -> Node:
        if len(self.heap) == 0:
            return None

        min = self.heap.pop(0)  # Extract the min element

        if len(self.heap) > 0:
            last = self.heap.pop()  # Extract the last element
            last.index = 0  # Update the index of node object
            self.heap.insert(0, last)

            self.__decrease_value(last)  # Heapify the node object

        return min.value

    def update(self, index, new_value: Node) -> None:
        if index >= len(self.heap):
            return None

        node = self.heap[index]  # Get the updated node
        prev_value = node.value  # Get the prev value
        node.value = new_value  # Update the value

        if new_value > prev_value:
            self.__increase_value(node)
        else:
            self.__decrease_value(node)

    def __increase_value(self, node: NodeHeap) -> None:
        # While node not the first and his parent is minor
        while node.index >= 1 and self.heap[node.parent].value > node.value:
            self.__swap(self.heap, node.index, node.parent)

    def __decrease_value(self, node: NodeHeap) -> None:
        while True:
            # If left child runs out
            if node.left >= len(self.heap):
                break

            # Only left child
            if node.right >= len(self.heap):
                nodeLeft = self.heap[node.left]
                if nodeLeft.value < node.value:
                    self.__swap(self.heap, node.index, node.left)
                else:
                    # If current node is bigger
                    break

            # Both children
            else:
                nodeLeft = self.heap[node.left]
                nodeRight = self.heap[node.right]

                # If the current node is lesser, finish the decrease
                if node.value < min(nodeLeft.value, nodeRight.value):
                    break

                # if left child is lesser, swap them
                if nodeLeft.value < nodeRight.value:
                    self.__swap(self.heap, node.index, node.left)
                # if right child is lesser, swap them
                else:
                    self.__swap(self.heap, node.index, node.right)

    def __swap(self, array, i, j):
        nodeI = self.heap[i]
        nodeJ = self.heap[j]

        # Inverte a posição do nodeI e nodeJ no array
        array[i], array[j] = array[j], array[i]
        # Atualiza a posição dos node dentro do objeto
        nodeJ.index, nodeI.index = nodeI.index, nodeJ.index

    def __len__(self) -> int:
        return len(self.heap)


class AStar:
    def __init__(self, matrix: list, empty_points: list, valid_initial: list) -> None:
        self.__matrix = matrix
        self.__x = len(matrix)
        self.__y = len(matrix[0])
        self.__end = ()
        self.__open_list = MinHeap([])
        self.__closed_nodes: List[Node] = []
        self.__empty_points = empty_points
        self.__valid_initial = valid_initial

    def search_path(self, start_position: tuple, end_position: tuple, diagonal=False) -> list:
        if not self.__validate_initial_positions([start_position, end_position]):
            print('Input Inválido')
            return []

        start_node = Node(start_position, None)

        self.__open_list = MinHeap([])
        self.__closed_nodes = []

        self.__open_list.insert(start_node)
        self.__end = end_position

        while len(self.__open_list) > 0:
            current_node = self.__open_list.popMinimum()
            self.__closed_nodes.append(current_node)

            if self.__check_finish(current_node, end_position):

                return self.__get_traceback(start_node, current_node)

            children = self.__search_children_sides(current_node)
            for child in children:
                self.__update_queue_side(current_node, child)

            if diagonal:
                children = self.__search_children_diagonal(current_node)
                for child in children:
                    self.__update_queue_diagonal(current_node, child)

        print('Retornando caminho vazio')
        return []

    def __search_children_sides(self, node: Node) -> list:
        children = []
        possible_positions = [
            (node.position[0], node.position[1] - 1),
            (node.position[0] - 1, node.position[1]),
            (node.position[0], node.position[1] + 1),
            (node.position[0] + 1, node.position[1]),
        ]

        for position in possible_positions:
            if self.__validate_position(position):
                if self.__not_in_closed(position):
                    child_node = Node(position, node)
                    children.append(child_node)

        return children

    def __search_children_diagonal(self, node: Node) -> list:
        children = []
        possible_positions = [
            (node.position[0] - 1, node.position[1] - 1),
            (node.position[0] + 1, node.position[1] + 1),
            (node.position[0] - 1, node.position[1] + 1),
            (node.position[0] + 1, node.position[1] - 1),
        ]

        for position in possible_positions:
            if self.__validate_position(position):
                if self.__not_in_closed(position):
                    child_node = Node(position, node)
                    children.append(child_node)

        return children

    def __update_queue_side(self, current_node: Node, child: Node) -> None:
        deltaX = abs(child.position[0] - self.__end[0]) ** 2
        deltaY = abs(child.position[1] - self.__end[1]) ** 2

        child.g = current_node.g + 1  # Distancia do inicio até o ponto
        child.h = (deltaX + deltaY)  # Distancia reta até o destino
        # child.f = child.g + child.h

        x = abs(child.position[0] - self.__end[0])
        y = abs(child.position[1] - self.__end[1])
        child.f = max(x, y) + (sqrt(2)-1)*min(x, y)
        # Procura o node que está sendo atualizado na lista de abertos
        for index, heapNode in enumerate(self.__open_list.heap):
            node = heapNode.value
            if node == child:
                if node.f > child.f or node.g > child.g:
                    self.__open_list.update(index, child)
                return None

        self.__open_list.insert(child)

    def __update_queue_diagonal(self, current_node, child: Node) -> None:
        deltaX = (child.position[0] - self.__end[0]) ** 2
        deltaY = (child.position[1] - self.__end[1]) ** 2

        child.g = current_node.g + 1.5
        child.h = (deltaX + deltaY)
        # child.f = child.g + child.h
        x = abs(child.position[0] - self.__end[0])
        y = abs(child.position[1] - self.__end[1])
        child.f = max(x, y) + (sqrt(2)-1)*min(x, y)

        node, index = self.__get_if_in_open(child)
        if node == None:
            self.__open_list.insert(child)
            return None
        else:
            if node.f > child.f or node.g > child.g:
                self.__open_list.update(index, child)

    def __check_finish(self, current_node, end_position) -> bool:
        return current_node.position == end_position

    def __get_traceback(self, start_node: Node, current_node: Node):
        path = []
        current = current_node

        while current != start_node:
            path.insert(0, current.position)
            current = current.parent

        return path

    def __validate_initial_positions(self, positions: list) -> bool:
        def validate_initial_position(position: tuple):
            if len(position) != 2:
                return False

            if position[0] < 0 or position[0] > self.__x - 1:
                return False

            if position[1] < 0 or position[1] > self.__y - 1:
                return False

            if self.__matrix[position[0]][position[1]] in self.__valid_initial:
                return True

            if self.__matrix[position[0]][position[1]] not in self.__empty_points:
                return False

            return True

        for position in positions:
            if not validate_initial_position(position):
                return False

        return True

    def __validate_position(self, position: tuple) -> bool:
        if len(position) != 2:
            return False

        if position[0] < 0 or position[0] > self.__x - 1:
            return False

        if position[1] < 0 or position[1] > self.__y - 1:
            return False

        if self.__matrix[position[0]][position[1]] not in self.__empty_points:
            return False

        return True

    def __not_in_closed(self, position: tuple):
        for node in self.__closed_nodes[::-1]:
            if node.position == position:
                return False
        return True

    def __get_if_in_open(self, position):
        for index, node in enumerate(self.__open_list.heap[::-1]):
            if node.value.position == position:
                return node.value, index

        return None, None


matriz_mapa_24 = [
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                PPPPPPPPPPPPP                  ', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                     J                         ', '                                               ',
    '                                               ', '              PPPPPPPPPPPPP                    ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
    '                                               ', '                                               ',
]


def main():
    inicio = (8, 22)
    fim = (12, 22)
    #inicio = (17, 13)
    #fim = (20, 19)

    searcher = AStar(matriz_mapa_24, [' ', 'J'], [' '])
    path, abertos = searcher.search_path(inicio, fim, True)

    print(len(abertos) - len(path))

    for ponto in abertos:
        antes = matriz_mapa_24[ponto[0]][0:ponto[1]]
        depois = matriz_mapa_24[ponto[0]][ponto[1]+1:]
        matriz_mapa_24[ponto[0]] = f'{antes}A{depois}'

    for ponto in path:
        antes = matriz_mapa_24[ponto[0]][0:ponto[1]]
        depois = matriz_mapa_24[ponto[0]][ponto[1]+1:]
        matriz_mapa_24[ponto[0]] = f'{antes}X{depois}'

    antes = matriz_mapa_24[inicio[0]][0:inicio[1]]
    depois = matriz_mapa_24[inicio[0]][inicio[1]+1:]
    matriz_mapa_24[inicio[0]] = f'{antes}I{depois}'

    antes = matriz_mapa_24[fim[0]][0:fim[1]]
    depois = matriz_mapa_24[fim[0]][fim[1]+1:]
    matriz_mapa_24[fim[0]] = f'{antes}F{depois}'

    for linha in matriz_mapa_24:
        print(linha)


if __name__ == '__main__':
    main()
