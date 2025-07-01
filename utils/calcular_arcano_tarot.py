import datetime

def calcular_arcano_tarot(data: datetime.date) -> int:
    soma = sum([int(d) for d in f"{data.day:02d}{data.month:02d}{data.year}"])
    while soma > 9:
        soma = sum([int(d) for d in str(soma)])
    return soma

