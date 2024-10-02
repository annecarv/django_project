from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices): ##está herdando
        TROCAR_VALVULA_MOTOR = "TVM", "Trocar Válvula do Motor"
        TROCAR_DE_OLEO = "TO", "Troca de Óleo"
        BALANCEAMENTO = "B", "Balanceamento"
        LIMPEZA_SIMPLES = "LS", "Limpeza Simples"
        LIMPEZA_COMPLETA = "LC", "Limpeza Completa"
