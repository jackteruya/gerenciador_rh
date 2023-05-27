from core.services import BaseService
from departamentos.domain.models import Departamentos


class DepartamentosService(BaseService):
    def __init__(self, repository):
        super(DepartamentosService, self).__init__(repository)
        self.model = Departamentos
