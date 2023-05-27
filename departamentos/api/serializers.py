from core.api.serializers import BaseSeralizer
from departamentos.domain.models import Departamentos


class DepartamentosSerializer(BaseSeralizer):
    class Meta:
        model = Departamentos
        fields = [
            'id',
            'centro_custo',
            'nome',
            'codigo_integracao',
            'empresa_id',
            'ativo',
        ]
        read_only_fields = ['id', 'ativo', ]
