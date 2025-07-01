from astropy.time import Time
from astropy.coordinates import get_sun
import astropy.units as u
import numpy as np
import datetime

def determinar_estacao_nascimento(data_nascimento: datetime.date) -> str:
    """
    Determina a estação astronômica exata com base na posição do Sol na data de nascimento.
    Usa a longitude eclíptica do Sol para detectar:
    - 0°   => Equinócio de março (outono sul / primavera norte)
    - 90°  => Solstício de junho
    - 180° => Equinócio de setembro
    - 270° => Solstício de dezembro

    Retorna: "Verão", "Outono", "Inverno", "Primavera" (baseado no hemisfério sul)
    """
    ano = data_nascimento.year
    datas = Time(f'{ano}-01-01') + np.linspace(0, 365, 500) * u.day
    longitudes = get_sun(datas).geocentrictrueecliptic.lon.deg

    estacoes = {
        "Outono": 0,
        "Inverno": 90,
        "Primavera": 180,
        "Verão": 270
    }

    data_input = Time(data_nascimento.isoformat())
    longitude_data = get_sun(data_input).geocentrictrueecliptic.lon.deg % 360

    for estacao, grau in reversed(estacoes.items()):
        if longitude_data >= grau:
            return estacao
    return "Verão"  # fallback para final de ano
