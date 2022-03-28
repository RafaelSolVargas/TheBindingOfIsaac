class Hitbox:
    def __init__(self, posicao: tuple, tamanho: tuple, transpassavel=False) -> None:
        self.__posicao = posicao
        self.__tamanho = tamanho
        self.__transpassavel = transpassavel

    @property
    def transpassavel(self) -> bool:
        return self.__transpassavel

    @transpassavel.setter
    def transpassavel(self, value) -> None:
        if type(value) == bool:
            self.__transpassavel = value

    @property
    def center(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] // 2
        y = self.__posicao[1] + self.__tamanho[1] // 2
        return (x, y)

    @property
    def topright(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0]
        y = self.__posicao[1]
        return (x, y)

    @property
    def topleft(self) -> tuple:
        return self.__posicao

    @property
    def bottomleft(self) -> tuple:
        x = self.__posicao[0]
        y = self.__posicao[1] + self.__tamanho[1]
        return (x, y)

    @property
    def bottomright(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0]
        y = self.__posicao[1] + self.__tamanho[1]
        return (x, y)

    @property
    def midright(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0]
        y = self.__posicao[1] + self.__tamanho[1] // 2
        return (x, y)

    @property
    def midbottomright(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0]
        y = self.__posicao[1] + self.__tamanho[1] * (3/4)
        return (int(x), int(y))

    @property
    def midtopright(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0]
        y = self.__posicao[1] + self.__tamanho[1] * (1/4)
        return (int(x), int(y))

    @property
    def midbottomleft(self) -> tuple:
        x = self.__posicao[0]
        y = self.__posicao[1] + self.__tamanho[1] * (3/4)
        return (int(x), int(y))

    @property
    def midtopleft(self) -> tuple:
        x = self.__posicao[0]
        y = self.__posicao[1] + self.__tamanho[1] * (1/4)
        return (int(x), int(y))

    @property
    def midlefttop(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] * (1/4)
        y = self.__posicao[1]
        return (int(x), int(y))

    @property
    def midrighttop(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] * (3/4)
        y = self.__posicao[1]
        return (int(x), int(y))

    @property
    def midleftbottom(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] * (1/4)
        y = self.__posicao[1] + self.__tamanho[1]
        return (int(x), int(y))

    @property
    def midrightbottom(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] * (3/4)
        y = self.__posicao[1] + self.__tamanho[1]
        return (int(x), int(y))

    @property
    def midbottom(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] // 2
        y = self.__posicao[1] + self.__tamanho[1]
        return (x, y)

    @property
    def midleft(self) -> tuple:
        x = self.__posicao[0]
        y = self.__posicao[1] + self.__tamanho[1] // 2
        return (x, y)

    @property
    def midtop(self) -> tuple:
        x = self.__posicao[0] + self.__tamanho[0] // 2
        y = self.__posicao[1]
        return (x, y)

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def tamanho(self) -> tuple:
        return self.__tamanho

    @posicao.setter
    def posicao(self, posicao: tuple) -> None:
        if type(posicao) == tuple and len(posicao) == 2:
            self.__posicao = posicao

    @property
    def x(self) -> int:
        return self.__posicao[0]

    @x.setter
    def x(self, x) -> None:
        if type(x) == int:
            nova_posicao = (x, self.__posicao[1])
            self.__posicao = nova_posicao

    @property
    def y(self) -> int:
        return self.__posicao[1]

    @y.setter
    def y(self, y) -> None:
        if type(y) == int:
            nova_posicao = (self.__posicao[0], y)
            self.__posicao = nova_posicao

    @property
    def altura(self) -> int:
        return self.__tamanho[1]

    @altura.setter
    def altura(self, altura) -> None:
        if type(altura) == int:
            novo_tamanho = (altura, self.__tamanho[0])
            self.__tamanho = novo_tamanho

    @property
    def largura(self) -> int:
        return self.__tamanho[0]

    @largura.setter
    def largura(self, largura) -> None:
        if type(largura) == int:
            novo_tamanho = (self.__tamanho[1], largura)
            self.__tamanho = novo_tamanho

    @property
    def left(self) -> int:
        return self.__posicao[0]

    @property
    def right(self) -> int:
        return self.__posicao[0] + self.__tamanho[0]

    @property
    def top(self) -> int:
        return self.__posicao[1]

    @property
    def bottom(self) -> int:
        return self.__posicao[1] + self.__tamanho[1]
