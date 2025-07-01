from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# 1. Configurar Jinja2 e carregar template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/template12.html')

# 2. Dados de exemplo
dados = {
    "nome": "Xanfox",
    "data_nascimento": "25 de maio de 1982",
    "hora_nascimento": "07:25",
    "local_nascimento": "São Paulo - SP",
    "signo_solar": "Gêmeos",
    "planeta_solar": "Mercúrio",
    "forca_solar": "Curiosidade ampla",
    "fraqueza_solar": "Distração crônica",
    "descricao_solar": "Você tem múltiplos interesses e se adapta rápido.",
    "signo_lunar": "Câncer",
    "descricao_lunar": "Você sente tudo com profundidade e cuida do que ama.",
    "ascendente": "Gêmeos",
    "descricao_ascendente": "Facilidade de comunicação e adaptabilidade.",
    "arcano_tarot": "O Hierofante",
    "mote_tarot": "Que o bom conselho te acompanhe.",
    "estilo_tarot": "Curioso, questionador, busca sabedoria.",
    "fraquezas_tarot": "Dogmatismo, impulsividade.",
    "descricao_tarot": "Você veio para ensinar e guiar — mas precisa aplicar o que aprende.",
    "signo_celta": "Hawthorn",
    "elemento_celta": "Vulcano",
    "animal_celta": "Abelha e Coruja",
    "descricao_celta": "Sensível, conectado à cura e às transições.",
    "signo_chines": "Cão",
    "elemento_chines": "Terra",
    "mantra_chines": "Sou leal ao meu destino.",
    "descricao_chines": "Fiel, intuitivo e com senso profundo de justiça.",
    "numero_caminho": "5",
    "forcas_numerologia": "Versatilidade, adaptabilidade, sociabilidade.",
    "desafios_numerologia": "Desorganização, instabilidade.",
    "descricao_numerologia": "Você está em constante movimento — e aprende vivendo."
}

# 3. Renderizar HTML com os dados
html_renderizado = template.render(dados)

# 4. Gerar PDF
HTML(string=html_renderizado).write_pdf("circulo_interior_teste.pdf")

print("✅ PDF gerado com sucesso!")

