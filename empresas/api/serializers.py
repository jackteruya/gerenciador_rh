from core.api.serializers import BaseSeralizer
from empresas.domain.models import Empresas


class EmpresasSerializer(BaseSeralizer):
    class Meta:
        model = Empresas
        fields = [
            'id',
            'cnpj',
            'logradouro',
            'cidade',
            'pais',
            'ativo',
        ]
