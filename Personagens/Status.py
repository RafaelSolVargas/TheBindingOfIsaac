class Status:
    def __init__(self, status: dict) -> None:
        if 'vida_maxima' in status.keys():
            self.__vida_maxima = status['vida_maxima']
        elif 'vida' in status.keys():
            self.__vida_maxima = status['vida']
        else:
            self.__vida_maxima = 0
        
        self.__vida = status['vida'] if 'vida' in status.keys() else 0
        self.__ataque = status['ataque'] if 'ataque' in status.keys() else 0
        self.__defesa = status['defesa'] if 'defesa' in status.keys() else 0
        self.__alcance = status['alcance'] if 'alcance' in status.keys() else 0
        self.__vel = status['vel'] if 'vel' in status.keys() else 0
        self.__vel_ataque = status['vel_ataque'] if 'vel_ataque' in status.keys() else 0
        self.__invencibilidade = False
        self.__transpassavel = status['transpassavel'] if 'transpassavel' in status.keys(
        ) else False

    def get_status_dict(self) -> dict:
        return {
            'vida': self.__vida,
            'vida_maxima': self.__vida_maxima,
            'ataque': 5,
            'defesa': 5,
            'vel': 3,
            'vel_ataque': 1,
            'transpassavel': False
        }
        

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, value: int) -> None:
        if type(value) == int and value > -1:
            self.__ataque = value

    @property
    def defesa(self) -> int:
        return self.__defesa

    @defesa.setter
    def defesa(self, value: int) -> None:
        if type(value) == int and value > -1:
            self.__defesa = value

    @property
    def alcance(self) -> int:
        return self.__alcance

    @alcance.setter
    def alcance(self, value: int) -> None:
        if type(value) == int and value > -1:
            self.__alcance = value

    @property
    def vida_maxima(self) -> int:
        return self.__vida_maxima

    @vida_maxima.setter
    def vida_maxima(self, value: int) -> None:
        if type(value) == int and value > -1:
            self.__vida_maxima = value

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, value: int) -> None:
        if value < self.__vida and self.__invencibilidade:
            return

        if type(value) == int:
            if value > self.__vida_maxima:
                self.__vida = self.__vida_maxima
            elif value < 0:
                self.__vida = 0
            else:
                self.__vida = value

    @property
    def vel(self) -> int:
        return self.__vel

    @vel.setter
    def vel(self, value: int) -> None:
        if type(value) == int:
            self.__vel = value

    @property
    def vel_ataque(self) -> int:
        return self.__vel_ataque

    @vel_ataque.setter
    def vel_ataque(self, value: int) -> None:
        if type(value) == int:
            self.__vel_ataque = value

    @property
    def invencibilidade(self) -> bool:
        return self.__invencibilidade

    @invencibilidade.setter
    def invencibilidade(self, value):
        if type(value) == bool:
            self.__invencibilidade = value

    @property
    def transpassavel(self) -> bool:
        return self.__transpassavel

    @transpassavel.setter
    def transpassavel(self, value):
        if type(value) == bool:
            self.__transpassavel = value
