import datetime

def calcular_caminho_de_vida(data: datetime.date) -> int:
    digitos = [int(d) for d in f"{data.day:02d}{data.month:02d}{data.year}"]
    soma = sum(digitos)

    # Redução numerológica (exceto números mestres)
    while soma > 9 and soma not in [11, 22, 33]:
        soma = sum([int(d) for d in str(soma)])
    
    return soma
