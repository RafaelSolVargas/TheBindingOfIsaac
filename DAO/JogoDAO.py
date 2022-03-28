from DAO.DAO import DAO
from Jogo.Jogo import Jogo
from DAO.DAOAdapters import JogoDaoAdapter


class JogoDAO(DAO):
    def __init__(self) -> None:
        super().__init__()

    def add(self, jogo: Jogo) -> None:
        if isinstance(jogo, Jogo):
            jogo_dao = JogoDaoAdapter.add(jogo)
            save_name = jogo.save_name
            super().add(save_name, jogo_dao)

    def get(self, key: str) -> Jogo:
        if isinstance(key, str):
            jogo_dao = super().get(key)
            jogo = JogoDaoAdapter.create(jogo_dao)
            return jogo

    def remove(self, key: str) -> None:
        if isinstance(key, str):
            return super().remove(key)
