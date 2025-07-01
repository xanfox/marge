import datetime
import pytz

# ==== Imports da flatlib ====
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

def determinar_signo_lunar(data: datetime.date, hora: str, latitude: float, longitude: float, fuso: str) -> dict:
    try:
        # Tradutor de signos do flatlib para português
        SIGNOS_LUNARES_PT = {
            "ARIES": "Áries",
            "TAURUS": "Touro",
            "GEMINI": "Gêmeos",
            "CANCER": "Câncer",
            "LEO": "Leão",
            "VIRGO": "Virgem",
            "LIBRA": "Libra",
            "SCORPIO": "Escorpião",
            "SAGITTARIUS": "Sagitário",
            "CAPRICORN": "Capricórnio",
            "AQUARIUS": "Aquário",
            "PISCES": "Peixes"
        }

        DESCRICOES = {
            "ARIES": "Emoções intensas, impulsividade e coragem. Lua em Áries indica alguém que sente com paixão.",
            "TAURUS": "Estabilidade emocional e afeto. Lua em Touro é ligada a conforto e segurança.",
            "GEMINI": "Emoções flutuantes, necessidade de comunicação. Lua em Gêmeos pensa antes de sentir.",
            "CANCER": "Profundamente emotiva e protetora. Lua em Câncer é o lar emocional.",
            "LEO": "Sentimentos expressivos e desejo de reconhecimento. Lua em Leão precisa brilhar.",
            "VIRGO": "Controle emocional e análise. Lua em Virgem sente através da lógica.",
            "LIBRA": "Busca harmonia emocional e evita conflitos. Lua em Libra precisa de equilíbrio.",
            "SCORPIO": "Emoções intensas, reservadas e transformadoras. Lua em Escorpião sente com profundidade.",
            "SAGITTARIUS": "Emoções otimistas e expansão. Lua em Sagitário busca liberdade afetiva.",
            "CAPRICORN": "Contida e responsável. Lua em Capricórnio sente com cautela.",
            "AQUARIUS": "Emoções distantes e racionais. Lua em Aquário precisa de espaço.",
            "PISCES": "Sensibilidade extrema e empatia. Lua em Peixes dissolve as fronteiras emocionais."
        }

        # Montar datetime com fuso
        dt_naive = datetime.datetime.combine(data, datetime.datetime.strptime(hora, "%H:%M").time())
        tz = pytz.timezone(fuso)
        dt_local = tz.localize(dt_naive)
        offset = dt_local.utcoffset().total_seconds() / 3600
        offset_str = str(int(offset)) if offset.is_integer() else str(offset)

        # Criar mapa astral com flatlib
        dt = Datetime(data.strftime('%Y/%m/%d'), hora, offset_str)
        pos = GeoPos(float(latitude), float(longitude))
        chart = Chart(dt, pos)

        lua = chart.get(const.MOON)
        signo_en = lua.sign.upper()
        signo_pt = SIGNOS_LUNARES_PT.get(signo_en, signo_en.title())

        return {
            "signo": signo_pt,
            "descricao": DESCRICOES.get(signo_en, "-")
        }

    except Exception as e:
        return {
            "signo": "-",
            "descricao": f"Erro ao calcular: {str(e)}"
        }

