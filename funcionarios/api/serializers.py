from core.api.serializers import BaseSeralizer
from funcionarios.domain.models import Funcionarios


class FuncionariosSerializer(BaseSeralizer):
    class Meta:
        model = Funcionarios
        fields = [
            'id',
            'nome',
            'sobrenome',
            'email',
            'telefone',
            'data_nascimento',
            'data_ingresso',
            'data_desligamento',
            'cidade',
            'departamento_id',
            'empresa_id',
            'ativo',
        ]
        read_only_fields = ['id', 'ativo', ]
