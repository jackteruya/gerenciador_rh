from core.domain.repository import BaseRepository


class FuncionariosRepository(BaseRepository):
    def __init__(self, model):
        self.model = model
