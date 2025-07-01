import datetime

# Ver signo da pessoa
def determinar_signo_solar(data: datetime.date) -> str:
    # Tabela de signos (ordem importa!)
    signos = [
        ((1, 20), "Capricórnio"),
        ((2, 18), "Aquário"),
        ((3, 20), "Peixes"),
        ((4, 19), "Áries"),
        ((5, 20), "Touro"),
        ((6, 20), "Gêmeos"),
        ((7, 22), "Câncer"),
        ((8, 22), "Leão"),
        ((9, 22), "Virgem"),
        ((10, 22), "Libra"),
        ((11, 21), "Escorpião"),
        ((12, 21), "Sagitário"),
        ((12, 31), "Capricórnio"),  # Capricórnio continua até 31/12
    ]

    for (mes_fim, dia_fim), signo in signos:
        if (data.month, data.day) <= (mes_fim, dia_fim):
            return signo
    return "Erro#!"  # fallback de segurança
