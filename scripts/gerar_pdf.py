# ==== Imports de caminhos ====
import os  # Necessário para os.remove e os.path.exists
from pypdf import PdfReader  # type: ignore
from utils.paths import SYSTEM_DIR, TEMPLATES_DIR, OUTPUT_DIR, DATA_DIR, BASE_DIR

# ==== Imports dicts do projeto ====
from scripts.dicts import PERFIL_NUMEROLOGICO, PLANETAS_REGENTES, PERFIL_SOLAR, ARCANOS_TAROT

import json
import datetime
import pandas as pd

OUTPUT_DIR.mkdir(exist_ok=True)

ESTADOS_CSV = SYSTEM_DIR / "estados.csv"
MUNICIPIOS_CSV = SYSTEM_DIR / "municipios.csv"

# >>> funções importadas de utils
from utils.gerar_pdf import gerar_pdf, coletar_paginas_do_sumario, criar_sumario_para_jinja
from utils.formatar_data_nascimento import formatar_data_nascimento
from utils.determinar_signo_solar import determinar_signo_solar
from utils.determinar_signo_lunar import determinar_signo_lunar
from utils.determinar_ascendente import determinar_ascendente
from utils.calcular_caminho_de_vida import calcular_caminho_de_vida
from utils.calcular_arcano_tarot import calcular_arcano_tarot
from utils.determinar_signo_celta import determinar_signo_celta
from utils.determinar_signo_chines import determinar_signo_chines
from utils.determinar_estacao_nascimento import determinar_estacao_nascimento

from utils.gerar_apresentacao_geral import gerar_apresentacao_geral
from utils.gerar_apresentacao_estacoes import gerar_apresentacao_estacao




def execute_single():
    print("\n🧙 MODO SIMPLIFICADO — Criação guiada de PDF")

    nome_input = input("➡️  Digite o nome completo: ").strip()
    nome_corrigido = ' '.join([parte.capitalize() for parte in nome_input.split()])

    # sexo
    while True:
        sexo_input = input("⚧️ Informe o sexo (M para masculino, F para feminino, Z para outro — padrão: feminino): ").strip().lower()
        if sexo_input == "":
            sexo = "f"
            break
        elif sexo_input in ["m", "f", "z"]:
            sexo = sexo_input
            break
        else:
            print("❌ Entrada inválida. Digite M, F, Z ou apenas Enter para padrão feminino.")
    
    from utils.pronomes import obter_pronomes
    pronomes = obter_pronomes(sexo)
    
    # === NOVO BLOCO DE LÓGICA: Determinar "Nascido" ou "Nascida" ===
    if sexo == 'm':
        nascimento_termo = "Nascido em"
    elif sexo == 'f':
        nascimento_termo = "Nascida em"
    else:
        nascimento_termo = "Nascidx em"
    # ================================================================

    # Carregar os arquivos CSV
    estados_df = pd.read_csv(ESTADOS_CSV)
    municipios_df = pd.read_csv(MUNICIPIOS_CSV)

    while True:
        data_input = input("📅 Digite a data de nascimento (ex: 25 de maio de 1982 ou 25051982): ").strip()
        try:
            data_corrigida, data_date = formatar_data_nascimento(data_input)
            break
        except ValueError:
            print("❌ Formato inválido. Tente novamente.")

    while True:
        estado_input = input("🗺️  Estado de nascimento (sigla, ex: SP): ").strip().upper()
        if estado_input in estados_df["uf"].values:
            break
        else:
            print("❌ Estado não encontrado. Tente novamente com a sigla (ex: RJ).")

    estado_cod = estados_df.loc[estados_df["uf"] == estado_input, "codigo_uf"].values[0]

    while True:
        municipio_input = input("🏙️  Município de nascimento: ").strip().title()
        municipio_df = municipios_df[
            (municipios_df["codigo_uf"] == estado_cod) &
            (municipios_df["nome"].str.title() == municipio_input)
        ]
        if not municipio_df.empty:
            municipio_info = municipio_df.iloc[0]
            break
        else:
            print("❌ Município não encontrado no estado informado. Tente novamente.")

    latitude = municipio_info["latitude"]
    longitude = municipio_info["longitude"]
    fuso_horario = municipio_info["fuso_horario"]

    while True:
        hora_input = input("🕰️ Digite a hora de nascimento (formato HH:MM) ou pressione X para desconhecida: ").strip()
        if hora_input.lower() == "x":
            hora_nascimento = "00:00"
            break
        try:
            hora_formatada = datetime.datetime.strptime(hora_input, "%H:%M")
            hora_nascimento = hora_formatada.strftime("%H:%M")
            break
        except ValueError:
            print("❌ Formato inválido. Use HH:MM (ex: 14:30) ou X para desconhecida.")

    signo_solar = determinar_signo_solar(data_date)
    planeta_regente = PLANETAS_REGENTES.get(signo_solar, "-")
    perfil_solar = PERFIL_SOLAR.get(signo_solar, {"forca": "-", "fraqueza": "-", "descricao": "-"})

    numero_caminho = calcular_caminho_de_vida(data_date)
    perfil = PERFIL_NUMEROLOGICO.get(numero_caminho, {"forcas": "-", "desafios": "-", "descricao": "-"})

    numero_arcano = calcular_arcano_tarot(data_date)
    arcano = ARCANOS_TAROT[numero_arcano]
    signo_celta = determinar_signo_celta(data_date)
    signo_chines = determinar_signo_chines(data_date.year)
    
    if hora_nascimento == "00:00":
        signo_lunar = {"signo": "-", "descricao": "Hora desconhecida — não foi possível calcular o signo lunar."}
        ascendente = {"ascendente": "-", "descricao": "Hora desconhecida — não foi possível calcular o ascendente."}
    else:
        signo_lunar = determinar_signo_lunar(data_date, hora_nascimento, latitude, longitude, fuso_horario)
        ascendente = determinar_ascendente(data_date, hora_nascimento, latitude, longitude, fuso_horario)

    local_nascimento = f"{municipio_input}/{estado_input}"

    estacao_ano = determinar_estacao_nascimento(data_date)
    apresenta_estacao = gerar_apresentacao_estacao(estacao_ano)

    dados = {
        "nome": nome_corrigido,
        "nascimento_termo": nascimento_termo,
        "data_nascimento": data_corrigida,
        "hora_nascimento": hora_nascimento,
        "local_nascimento": local_nascimento,
        "latitude": latitude,
        "longitude": longitude,
        "fuso_horario": fuso_horario,
        "apresentacao_geral": gerar_apresentacao_geral(nome_corrigido, pronomes),
        "estacao_ano": estacao_ano,
        "apresentacao_estacao": apresenta_estacao,
        "signo_solar": signo_solar,
        "planeta_solar": planeta_regente,
        "forca_solar": perfil_solar["forca"],
        "fraqueza_solar": perfil_solar["fraqueza"],
        "descricao_solar": perfil_solar["descricao"],
        "signo_lunar": signo_lunar["signo"],
        "descricao_lunar": signo_lunar["descricao"],
        "ascendente": ascendente["ascendente"],
        "descricao_ascendente": ascendente["descricao"],
        "arcano_tarot": arcano["arcano"],
        "mote_tarot": arcano["mote"],
        "estilo_tarot": arcano["estilo"],
        "fraquezas_tarot": arcano["fraquezas"],
        "descricao_tarot": arcano["descricao"],
        "cor_celta": signo_celta["cor"],
        "flor_celta": signo_celta["flor"],
        "celestial_celta": signo_celta["celestial"],
        "signo_celta": signo_celta["signo"],
        "elemento_celta": signo_celta["elemento"],
        "animal_celta": signo_celta["animal"],
        "descricao_celta": signo_celta["descricao"],
        "signo_chines": signo_chines["animal"],
        "elemento_chines": signo_chines["elemento"],
        "mantra_chines": signo_chines["mantra"],
        "descricao_chines": signo_chines["descricao"],
        "numero_caminho": str(numero_caminho),
        "forcas_numerologia": perfil["forcas"],
        "desafios_numerologia": perfil["desafios"],
        "descricao_numerologia": perfil["descricao"],
        "ascendente_mapa_astral": ascendente.get("ascendente_mapa_astral", None),
        "meio_ceu": None,
        "planetas_nos_signos_e_casas": None,
        "casas_astrologicas": None,
        "aspectos_principais": None,
        "imagem_textura": "textura.png",
        "sumario_com_paginas": [],   # será preenchido abaixo
        "total_pages": None,         # idem
        "is_first_pass": True        # começa em True para coletar sumário
    }

    # === NOVA SEÇÃO: coletar sumário dinâmico ===
    print("\n🔍 Coletando sumário dinâmico das seções…")
    mapa_paginas = coletar_paginas_do_sumario(dados)
    dados["sumario_com_paginas"] = criar_sumario_para_jinja(mapa_paginas)
    dados["is_first_pass"] = False
    print(f"📑 Sumário com {len(dados['sumario_com_paginas'])} itens gerado.")

    # nome dos PDFs
    temp_pdf_filename = OUTPUT_DIR / f"temp_circulo_interior_{nome_corrigido.replace(' ', '_')}.pdf"
    nome_pdf_final  = OUTPUT_DIR / f"circulo_interior_{nome_corrigido.replace(' ', '_')}.pdf"

    # === primeira geração física (para contar páginas) ===
    print(f"\n⚙️  Gerando PDF temporário para contagem de páginas…")
    gerar_pdf(dados.copy(), temp_pdf_filename, total_pages=None)

    try:
        total_pages = len(PdfReader(temp_pdf_filename).pages)
        print(f"📏 Total de páginas detectado: {total_pages}")
    except Exception as e:
        print(f"❌ Erro ao ler temporário: {e}")
        total_pages = '?'
    finally:
        if os.path.exists(temp_pdf_filename):
            os.remove(temp_pdf_filename)
            print(f"🗑️ Temporário removido: {temp_pdf_filename.name}")

    # === geração final com total_pages ===
    print(f"\n📄 Gerando PDF final…")
    dados["total_pages"] = total_pages
    print(f"🗓️ Estação detectada: {dados['estacao_ano']}")
    gerar_pdf(dados, nome_pdf_final, total_pages=total_pages)

    print("\n" + "="*50)
    print("🎉 PDF gerado com sucesso!\n")
    print(f"📄 Caminho do PDF final: {nome_pdf_final}")
    # ... restante do seu print de confirmação inalterado ...

# (o restante do arquivo: executar_legacy(), executar_batch() e main() continuam iguais)

    print(f"👤 Nome: {nome_corrigido}")
    print(f"🎂 Data: {data_corrigida} às {hora_nascimento if hora_nascimento != '00:00' else 'Desconhecida'}")
    print(f"🌍 Local: {local_nascimento} — LAT {latitude}, LONG {longitude} — Fuso: {fuso_horario}")
    print("\n☀️ SIGNO SOLAR:", signo_solar)
    print(f"   • Planeta: {planeta_regente}")
    print(f"   • Força: {perfil_solar['forca']}")
    print(f"   • Fraqueza: {perfil_solar['fraqueza']}")
    print(f"   • {perfil_solar['descricao']}")
    print("\n🔢 CAMINHO DE VIDA:", numero_caminho)
    print(f"   • Forças: {perfil['forcas']}")
    print(f"   • Desafios: {perfil['desafios']}")
    print(f"   • {perfil['descricao']}")
    print("\n🎴 ARCANO:", arcano['arcano'])
    print(f"   • {arcano['mote']} — {arcano['estilo']} — {arcano['fraquezas']}")
    print(f"   • {arcano['descricao']}")
    print("\n🌳 SIGNO CELTA:", signo_celta['signo'])
    print(f"   • {signo_celta['descricao']}")
    print("\n🐉 SIGNO CHINÊS:", signo_chines['animal'])
    print(f"   • Elemento: {signo_chines['elemento']}")
    print(f"   • Mantra: {signo_chines['mantra']}")
    print(f"   • {signo_chines['descricao']}")
    print("="*50)
    print(f"\n🌙 SIGNO LUNAR: {signo_lunar['signo']}")
    print(f"   • {signo_lunar['descricao']}")
    print(f"\n↗️ ASCENDENTE: {ascendente['ascendente']}")
    print(f"   • {ascendente['descricao']}")


def executar_legacy():
    print("\n📥 MODO LEGACY — Informe o nome do arquivo JSON em /data")
    nome_arquivo = input("Digite o nome do arquivo (ex: dados_usuario.json): ").strip()
    caminho_json = DATA_DIR / nome_arquivo

    if not caminho_json.exists():
        print("❌ Arquivo não encontrado:", caminho_json)
        return

    with open(caminho_json, encoding='utf-8') as f:
        dados = json.load(f)

    nome_corrigido = dados.get("nome", "desconhecido").replace(' ', '_')
    nome_pdf_final = OUTPUT_DIR / f"circulo_interior_{nome_corrigido}.pdf"

    # >>> MODIFICAÇÃO: Lógica de duas passagens para MODO LEGACY
    temp_pdf_filename = OUTPUT_DIR / f"temp_circulo_interior_{nome_corrigido}_legacy.pdf"
    print(f"Gerando PDF temporário para '{nome_corrigido}' (Modo Legacy)...")
    gerar_pdf(dados.copy(), temp_pdf_filename, total_pages=None)

    total_pages = 0
    try:
        reader = PdfReader(temp_pdf_filename)
        total_pages = len(reader.pages)
        print(f"Total de páginas detectado: {total_pages}")
    except Exception as e:
        print(f"❌ Erro ao ler PDF temporário (Legacy): {e}")
        total_pages = '?'
    finally:
        if os.path.exists(temp_pdf_filename):
            os.remove(temp_pdf_filename)
            print(f"PDF temporário '{temp_pdf_filename.name}' removido.")

    print(f"Gerando PDF final para '{nome_corrigido}' (Modo Legacy)...")
    gerar_pdf(dados, nome_pdf_final, total_pages=total_pages)
    print(f"✅ PDF final gerado com sucesso: {nome_pdf_final}")
    # >>> FIM DA LÓGICA DE DUAS PASSAGENS PARA MODO LEGACY


def executar_batch():
    print("\n📦 MODO LOTE — Gerando todos os arquivos JSON em /data")
    arquivos = list(DATA_DIR.glob("*.json"))

    if not arquivos:
        print("⚠️ Nenhum arquivo .json encontrado em /data")
        return

    for arquivo in arquivos:
        with open(arquivo, encoding='utf-8') as f:
            dados = json.load(f)
        
        nome_corrigido = dados.get("nome", "desconhecido").replace(' ', '_')
        nome_pdf_final = OUTPUT_DIR / f"circulo_interior_{nome_corrigido}.pdf"

        # >>> MODIFICAÇÃO: Lógica de duas passagens para MODO LOTE
        temp_pdf_filename = OUTPUT_DIR / f"temp_circulo_interior_{nome_corrigido}_batch.pdf"
        print(f"Gerando PDF temporário para '{nome_corrigido}' (Modo Lote)...")
        gerar_pdf(dados.copy(), temp_pdf_filename, total_pages=None)

        total_pages = 0
        try:
            reader = PdfReader(temp_pdf_filename)
            total_pages = len(reader.pages)
            print(f"Total de páginas detectado: {total_pages}")
        except Exception as e:
            print(f"❌ Erro ao ler PDF temporário (Lote): {e}")
            total_pages = '?'
        finally:
            if os.path.exists(temp_pdf_filename):
                os.remove(temp_pdf_filename)
                print(f"PDF temporário '{temp_pdf_filename.name}' removido.")

        print(f"Gerando PDF final para '{nome_corrigido}' (Modo Lote)...")
        gerar_pdf(dados, nome_pdf_final, total_pages=total_pages)
        print(f"✅ PDF final gerado com sucesso: {nome_pdf_final}")
        # >>> FIM DA LÓGICA DE DUAS PASSAGENS PARA MODO LOTE


# Para teste direto do script:
if __name__ == "__main__":
    # >>> MODIFICAÇÃO: Menu para escolher o modo
    while True:
        print("\nEscolha o modo de execução:")
        print("1. Modo Simplificado (Criação guiada)")
        print("2. Modo Legacy (Gerar PDF a partir de JSON existente)")
        print("3. Modo Lote (Gerar PDFs para todos os JSONs)")
        print("0. Sair")
        escolha = input("Digite o número da opção: ").strip()

        if escolha == '1':
            execute_single()
        elif escolha == '2':
            executar_legacy()
        elif escolha == '3':
            executar_batch()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")