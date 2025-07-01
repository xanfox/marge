import os
from jinja2 import Environment, FileSystemLoader

# --- Simulação do diretório de templates ---
# Assumimos que o script está na mesma pasta do diretório 'templates'
# ou ajuste o caminho para o seu TEMPLATES_DIR real.
TEMPLATES_DIR = os.path.join(os.getcwd(), 'templates') # Exemplo: ./templates/
if not os.path.exists(TEMPLATES_DIR):
    print(f"Diretório de templates não encontrado em: {TEMPLATES_DIR}")
    print("Por favor, crie uma pasta chamada 'templates' e coloque o arquivo 'template.html' dentro dela.")
    exit()

# --- 1. Dados de exemplo (Mockup) para o template ---
# Preencha este dicionário com valores que você quer testar
dados_mockup = {
    "nome": "João da Silva",
    "data_nascimento": "01 de Janeiro de 1990",
    "hora_nascimento": "12:00",
    "local_nascimento": "Rio de Janeiro/RJ",
    "imagem_textura": "file://" + os.path.abspath("assets/black-thread-light.png").replace("\\", "/"),
    "pages": "12",  # Simula a segunda passagem com o número total de páginas

    # Conteúdo das seções
    "apresentacao_geral": "Bem-vindo, João da Silva. Este é o seu Círculo Interior...",
    
    # Seção 2: Signo Solar
    "signo_solar": "Gêmeos",
    "planeta_solar": "Mercúrio",
    "forca_solar": "Comunicação, curiosidade, versatilidade.",
    "fraqueza_solar": "Dispersão, superficialidade, ansiedade.",
    "descricao_solar": "Gêmeos vive de ideias, trocas e movimento. Sua mente ágil encanta, mas precisa de foco e profundidade para florescer de verdade.",
    
    # Seção 3: Signo Lunar
    "signo_lunar": "Câncer",
    "descricao_lunar": "Profundamente emotiva e protetora. Lua em Câncer é o lar emocional.",
    
    # Seção 4: Ascendente
    "ascendente": "Gêmeos",
    "descricao_ascendente": "Expressivo e curioso. Ascendente em Gêmeos traz leveza, fala ágil e inquietação.",
    
    # Seção 5: Tarot
    "arcano_tarot": "O Hierofante",
    "mote_tarot": "Tradição, sabedoria, propósito.",
    "estilo_tarot": "Conselheiro, professor, guia.",
    "fraquezas_tarot": "Dogmatismo, inflexibilidade.",
    "descricao_tarot": "Sua missão é ensinar com sabedoria e humildade.",
    
    # Seção 6: Horóscopo Celta
    "signo_celta": "Espinheiro",
    "elemento_celta": "Topázio",
    "animal_celta": "Abelha, Coruja",
    "cor_celta": "Roxo",
    "flor_celta": "Trevo",
    "celestial_celta": "Vulcano",
    "descricao_celta": "Você nasceu sob a árvore sagrada Espinheiro, com a energia do(a) abelha, coruja, a cor roxo, a flor trevo, a pedra topázio e a influência celestial de Vulcano.",
    
    # Seção 7: Horóscopo Chinês
    "signo_chines": "Cão",
    "elemento_chines": "Água",
    "mantra_chines": "Eu sou leal ao que acredito",
    "descricao_chines": "Fiel e justo, o Cão protege o que ama com bravura.",
    
    # Seção 8: Caminho de Vida
    "numero_caminho": "5",
    "forcas_numerologia": "Liberdade, adaptabilidade, movimento.",
    "desafios_numerologia": "Instabilidade, impulsividade, vícios.",
    "descricao_numerologia": "Você veio para viver mudanças e inspirar liberdade. Sua missão é aprender com a experiência.",
    
    # Seção 9: Mapa Astral Completo
    "ascendente_mapa_astral": "Gêmeos",
    "meio_ceu": "Aquário",
    "planetas_nos_signos_e_casas": "Sol em Gêmeos na Casa 1...",
    "casas_astrologicas": "Casa 1 em Gêmeos, Casa 2 em Câncer...",
    "aspectos_principais": "Sol em conjunção com Mercúrio...",
}

# --- 2. Configuração do Jinja2 e renderização ---
try:
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template('sec01.html')
    html_renderizado = template.render(dados_mockup)

    # --- 3. Salvar o HTML renderizado em um arquivo ---
    output_filename = "visualizacao_template.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_renderizado)

    print(f"✅ Arquivo HTML gerado com sucesso: {output_filename}")
    print("Abra este arquivo no seu navegador para visualizar o resultado.")

except Exception as e:
    print(f"❌ Ocorreu um erro ao renderizar o template: {e}")
    print("Verifique se o arquivo 'template.html' está na pasta 'templates' e se as variáveis Jinja2 no template correspondem às chaves no dicionário 'dados_mockup'.")
