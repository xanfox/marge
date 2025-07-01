from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from utils.paths import TEMPLATES_DIR, BASE_DIR
import copy

# Lista de seções e IDs: mantenha em sync com seu template
SECOES_DO_SUMARIO = [
    ('01. Apresentação Geral', 'apresentacao'),
    ('02. Sua Estação', 'estacao'),
    ('03. Signo Solar', 'solar'),
    ('04. Signo Lunar', 'lunar'),
    ('05. Ascendente', 'ascendente'),
    ('06. Carta de Nascimento (Tarot)', 'tarot'),
    ('07. Horóscopo Celta', 'celta'),
    ('08. Horóscopo Chinês', 'chines'),
    ('09. Caminho de Vida', 'vida'),
    ('10. Extras - Como Tirar o Melhor Proveito Deste Material', 'extras'),
    ('11. Sobre o Autor', 'sobre_o_autor')
]

def gerar_pdf(dados, nome_saida, total_pages=None):
    """
    Gera o PDF com base nos dados fornecidos.
    Aceita um `total_pages` opcional para a paginação final.
    """
    textura_path = BASE_DIR / "assets" / "black-thread-light.png"
    dados["imagem_textura"] = f"file://{textura_path}"

    # Total pages
    if total_pages is not None and isinstance(total_pages, int) and total_pages > 0:
        dados['pages'] = str(total_pages)
    else:
        dados['pages'] = ''

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template('seasons.html')
    html_content = template.render(dados)

    base_url = f"file://{BASE_DIR}/"
    HTML(string=html_content, base_url=base_url).write_pdf(str(nome_saida))
    print(f"✅ PDF gerado: {nome_saida}")


def coletar_paginas_do_sumario(dados):
    """
    Renderiza em memória e retorna mapa { section_id: page_number }.
    """
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template('seasons.html')

    dados_pass1 = copy.deepcopy(dados)
    dados_pass1['is_first_pass'] = True
    dados_pass1['pages'] = ''

    html = template.render(dados_pass1)
    document = HTML(string=html, base_url=f"file://{BASE_DIR}/").render()

    mapa = {}
    for titulo, section_id in SECOES_DO_SUMARIO:
        pagina_encontrada = None
        for idx, page in enumerate(document.pages, start=1):
            def encontrou(box):
                el = getattr(box, 'element', None)
                if el is not None and el.get('id') == section_id:
                    return True
                for child in getattr(box, 'children', []):
                    if encontrou(child):
                        return True
                return False
            if encontrou(page._page_box):
                pagina_encontrada = idx
                break
        mapa[section_id] = pagina_encontrada or '?'
    return mapa


def criar_sumario_para_jinja(mapa_paginas):
    """
    Converte mapa de páginas em lista de dicts para o template.
    """
    sumario = []
    for titulo, section_id in SECOES_DO_SUMARIO:
        sumario.append({
            'titulo': titulo,
            'pagina': mapa_paginas.get(section_id, '?')
        })
    return sumario
