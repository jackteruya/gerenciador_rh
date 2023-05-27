from core.domain.repository import BaseRepository


class DepartamentosRepository(BaseRepository):
    def __init__(self, model):
        self.model = model
