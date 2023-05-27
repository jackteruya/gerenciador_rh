from core.domain.repository import BaseRepository


class EmpresasRepository(BaseRepository):
    def __init__(self, model):
        self.model = model
