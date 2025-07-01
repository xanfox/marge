import datetime
import pytz

# ==== Imports da flatlib ====
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

def determinar_ascendente(data: datetime.date, hora: str, latitude: float, longitude: float, fuso: str) -> dict:
    try:
        SIGNOS_ASCENDENTE_PT = {
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
            "ARIES": "Aparência marcante e atitude direta. Ascendente em Áries traz impulso, coragem e liderança.",
            "TAURUS": "Olhar sereno e presença firme. Ascendente em Touro indica estabilidade, sensualidade e resistência.",
            "GEMINI": "Expressivo e curioso. Ascendente em Gêmeos traz leveza, fala ágil e inquietação.",
            "CANCER": "Olhos profundos e energia acolhedora. Ascendente em Câncer é emotivo, protetor e intuitivo.",
            "LEO": "Postura nobre e brilho natural. Ascendente em Leão inspira confiança e carisma.",
            "VIRGO": "Detalhista e reservado. Ascendente em Virgem traz lógica, organização e discrição.",
            "LIBRA": "Elegante e equilibrado. Ascendente em Libra atrai com charme e senso estético.",
            "SCORPIO": "Intenso e misterioso. Ascendente em Escorpião transforma o ambiente com presença forte.",
            "SAGITTARIUS": "Expansivo e espontâneo. Ascendente em Sagitário é otimista e ama liberdade.",
            "CAPRICORN": "Sério e determinado. Ascendente em Capricórnio busca segurança, status e estrutura.",
            "AQUARIUS": "Original e imprevisível. Ascendente em Aquário quebra padrões com ideias inovadoras.",
            "PISCES": "Suave e sonhador. Ascendente em Peixes capta o invisível e vive através da intuição."
        }

        # Ajustar data/hora com fuso
        dt_naive = datetime.datetime.combine(data, datetime.datetime.strptime(hora, "%H:%M").time())
        tz = pytz.timezone(fuso)
        dt_local = tz.localize(dt_naive)
        offset = dt_local.utcoffset().total_seconds() / 3600
        offset_str = str(int(offset)) if offset.is_integer() else str(offset)

        # Criar carta astral
        dt = Datetime(data.strftime('%Y/%m/%d'), hora, offset_str)
        pos = GeoPos(float(latitude), float(longitude))
        chart = Chart(dt, pos)

        asc = chart.get(const.ASC)
        signo_en = asc.sign.upper()
        signo_pt = SIGNOS_ASCENDENTE_PT.get(signo_en, signo_en.title())

        return {
            "ascendente": signo_pt,
            "descricao": DESCRICOES.get(signo_en, "-")
        }

    except Exception as e:
        return {
            "ascendente": "-",
            "descricao": f"Erro ao calcular: {str(e)}"
        }
