from Config.Opcoes import Opcoes

class Converter:
    __opcoes = Opcoes()

    @classmethod
    def alcance_to_vector_dist(cls, alcance: int) -> int:
        ratio = 100 / (cls.__opcoes.MAX_ALCANCE - cls.__opcoes.MIN_ALCANCE)
        aumento = alcance / ratio

        return cls.__opcoes.MIN_ALCANCE + aumento

    @classmethod
    def vel_ataque_to_delay(cls, vel_ataque: int) -> int:
        ratio = 10 / (cls.__opcoes.MAX_DELAY_ATAQUE - cls.__opcoes.MIN_DELAY_ATAQUE)
        velocidade = vel_ataque / ratio

        return cls.__opcoes.MAX_DELAY_ATAQUE - velocidade