def obter_pronomes(sexo: str) -> dict:
    """Retorna pronomes e artigos de acordo com o sexo informado."""
    sexo = sexo.lower()
    
    if sexo == "m":
        return {
            "pronome_bemvindo": "Bem-vindo",
            "pronome_artigo": "o",
            "pronome_sujeito": "ele",
            "pronome_objeto": "nele",
        }
    elif sexo == "z":
        return {
            "pronome_bemvindo": "Bem-vindx",
            "pronome_artigo": "@",
            "pronome_sujeito": "elu",
            "pronome_objeto": "nilu",
        }
    else:  # feminino como padrão
        return {
            "pronome_bemvindo": "Bem-vinda",
            "pronome_artigo": "a",
            "pronome_sujeito": "ela",
            "pronome_objeto": "nela",
        }
