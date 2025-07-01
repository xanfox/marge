from scripts.dicts import ANIMAIS_CHINESES, ELEMENTOS_CHINESES


def determinar_signo_chines(ano: int) -> dict:
    base_ano = 1984  # ano do Rato de Madeira (início de um novo ciclo sexagenário)
    offset = ano - base_ano

    animal = ANIMAIS_CHINESES[offset % 12]
    elemento = ELEMENTOS_CHINESES[offset % 10]

    MANTRAS = {
        "Rato": "Eu penso antes de agir",
        "Boi": "Eu construo com paciência",
        "Tigre": "Eu ajo com coragem",
        "Coelho": "Eu acolho com delicadeza",
        "Dragão": "Eu lidero com paixão",
        "Serpente": "Eu intuo com sabedoria",
        "Cavalo": "Eu sigo livre",
        "Cabra": "Eu sinto com profundidade",
        "Macaco": "Eu inovo com astúcia",
        "Galo": "Eu brilho com autenticidade",
        "Cão": "Eu sou leal ao que acredito",
        "Porco": "Eu celebro a simplicidade",
    }

    DESCRICOES = {
        "Rato": "Ágil, adaptável e inteligente, o Rato usa sua lógica para prosperar.",
        "Boi": "Determinado, calmo e confiável, o Boi avança firme rumo a seus objetivos.",
        "Tigre": "Valente e impulsivo, o Tigre inspira respeito por onde passa.",
        "Coelho": "Amável e artístico, o Coelho preza por harmonia e beleza.",
        "Dragão": "Forte e visionário, o Dragão simboliza poder e transformação.",
        "Serpente": "Misteriosa e estratégica, a Serpente age com precisão.",
        "Cavalo": "Independente e carismático, o Cavalo busca sua própria estrada.",
        "Cabra": "Empática e sensível, a Cabra transforma o mundo com ternura.",
        "Macaco": "Perspicaz e brincalhão, o Macaco resolve desafios com humor.",
        "Galo": "Observador e direto, o Galo lidera com disciplina.",
        "Cão": "Fiel e justo, o Cão protege o que ama com bravura.",
        "Porco": "Gentil e pacífico, o Porco aprecia os prazeres da vida com doçura."
    }

    return {
        "animal": animal,
        "elemento": elemento,
        "mantra": MANTRAS.get(animal, "-"), 
        "descricao": DESCRICOES.get(animal, "-")
    }

