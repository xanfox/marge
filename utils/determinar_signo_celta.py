import datetime


def determinar_signo_celta(data: datetime.date) -> dict:
    # Signos com todos os atributos visuais/esotéricos da imagem
    signos = [
        ((12, 24), (1, 20), "Bétula", "Águia Dourada, Cervo Branco", "Branco", "Visco", "Cristal de Rocha", "Sol"),
        ((1, 21), (2, 17), "Sorveira", "Grou, Dragão Verde", "Cinza", "Perpétua", "Peridoto", "Lua"),
        ((2, 18), (3, 17), "Freixo", "Cavalo-marinho, Gaivota", "Verde", "Água-marinha", "Coral", "Netuno"),
        ((3, 18), (4, 14), "Amieiro", "Urso, Raposa, Falcão", "Laranja", "Papoila", "Rubi", "Marte"),
        ((4, 15), (5, 12), "Salgueiro", "Víbora, Lebre, Serpente Marinha", "Azul", "Flor-de-lis", "Pedra da Lua", "Lua"),
        ((5, 13), (6, 9), "Espinheiro", "Abelha, Coruja", "Roxo", "Trevo", "Topázio", "Vulcano"),
        ((6, 10), (7, 7), "Carvalho", "Ferreirinho, Lontra, Cavalo", "Dourado", "Rosa", "Diamante", "Júpiter"),
        ((7, 8), (8, 4), "Azevinho", "Gato, Unicórnio", "Prata", "Lírio", "Cornalina", "Saturno"),
        ((8, 5), (9, 1), "Aveleira", "Grou, Salmão", "Verde-musgo", "Lavanda", "Ametista", "Mercúrio"),
        ((9, 2), (9, 29), "Videira", "Lagarto, Cão, Cisne Branco", "Verde-claro", "Hortênsia", "Esmeralda", "Vênus"),
        ((9, 30), (10, 27), "Hera", "Javali, Borboleta, Ganso", "Preto", "Orquídea", "Opala", "Plutão"),
        ((10, 28), (11, 24), "Junco", "Cão de Caça, Coruja", "Marrom", "Girassol", "Jaspe", "Saturno"),
        ((11, 25), (12, 23), "Sabugueiro", "Texugo, Cavalo Negro, Corvo", "Laranja-queimado", "Cravo", "Ônix", "Urano"),
    ]

    for (m_start, d_start), (m_end, d_end), arvore, animal, cor, flor, pedra, celestial in signos:
        data_ano = data.replace(year=2000)
        inicio = datetime.date(2000, m_start, d_start)
        fim = datetime.date(2000, m_end, d_end)

        if inicio <= data_ano <= fim or (m_start > m_end and (data_ano >= inicio or data_ano <= fim)):
            return {
                "signo": arvore,
                "animal": animal,
                "elemento": pedra,
                "cor": cor,
                "flor": flor,
                "celestial": celestial,
                "descricao": (
                    f"Você nasceu sob a árvore sagrada {arvore}, com a energia do(a) {animal.lower()}, "
                    f"a cor {cor.lower()}, a flor {flor.lower()}, a pedra {pedra.lower()} "
                    f"e a influência celestial de {celestial}."
                )
            }

    return {
        "signo": "Desconhecido",
        "animal": "-",
        "elemento": "-",
        "cor": "-",
        "flor": "-",
        "celestial": "-",
        "descricao": "-"
    }
    

