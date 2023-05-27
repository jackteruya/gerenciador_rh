from core.services import BaseService
from funcionarios.domain.models import Funcionarios


class FuncionariosService(BaseService):
    def __init__(self, repository):
        super(FuncionariosService, self).__init__(repository)
        self.model = Funcionarios
