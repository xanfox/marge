

from scripts.dicts import ESTACOES_DESCRICOES

def gerar_apresentacao_estacao(estacao: str) -> str:
    """
    Retorna um bloco HTML com a descrição da estação fornecida.

    Parâmetros:
      - estacao: nome da estação ("Verão", "Outono", "Inverno" ou "Primavera").

    Retorna:
      - String contendo HTML formatado com o título e a descrição da estação.
    """
    descricao = ESTACOES_DESCRICOES.get(estacao, "")
    if not descricao:
        return ""
    return f"""
<div class="card full">
  <h2>2. 🍃 Estação do Ano: {estacao}</h2>
  <p>{descricao}</p>
</div>
"""
