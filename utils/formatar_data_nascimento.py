import datetime

def formatar_data_nascimento(data_input: str) -> str:
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    formatos_aceitos = [
        "%d%m%Y", "%d/%m/%Y", "%d-%m-%Y", "%d %m %Y",
        "%d de %B de %Y", "%d %B %Y"
    ]

    for formato in formatos_aceitos:
        try:
            dt = datetime.datetime.strptime(data_input, formato)
            break
        except ValueError:
            continue
    else:
        raise ValueError("Formato de data inválido.")

    return f"{dt.day} de {meses_pt[dt.month]} de {dt.year}", dt.date()
