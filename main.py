import json
import select

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


# Caminho para o arquivo de configuração
CONFIG_PATH = Path(__file__).parent / "system_config_jsons" / "config.json"


# Modos disponíveis
MODOS = {
    "1": "simplificado",
    "2": "legacy",
    "3": "batch"
}

DEFAULT_TIMEOUT = 5
modo_ativo = None

def carregar_config():
    try:
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, encoding='utf-8') as f:
                config = json.load(f)
            return config.get("modo_execucao", "legacy")
    except json.JSONDecodeError:
        print("⚠️ config.json corrompido. Usando 'legacy' como padrão.")
    return "legacy"




def salvar_config(modo):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)  # Garante que o diretório exista
    with open(CONFIG_PATH, "w", encoding='utf-8') as f:
        json.dump({"modo_execucao": modo}, f, indent=2)


def esperar_tecla(timeout=DEFAULT_TIMEOUT):
    global modo_ativo
    ultimo_modo = carregar_config()

    print("\n🔧 Pressione:")
    print("   1 - SIMPLIFICADO")
    print("   2 - LEGACY")
    print("   3 - LOTE")
    print(f"⏳ Ou aguarde {timeout} segundos para iniciar no modo anterior: {ultimo_modo.upper()}")
    print(">>> ", end='', flush=True)

    i, o, e = select.select([sys.stdin], [], [], timeout)
    if i:
        tecla = sys.stdin.readline().strip()
        modo_ativo = MODOS.get(tecla, ultimo_modo)
    else:
        modo_ativo = ultimo_modo

def iniciar_programa():
    print(f"\n🚀 Iniciando o sistema em modo: {modo_ativo.upper()}")
    salvar_config(modo_ativo)

    # Importa os modos de operação de forma tardia (evita carregamento desnecessário)
    from scripts.gerar_pdf import executar_legacy, executar_batch, execute_single

    if modo_ativo == "legacy":
        executar_legacy()
    elif modo_ativo == "batch":
        executar_batch()
    elif modo_ativo == "simplificado":
        execute_single()
    else:
        print("❌ Modo inválido.")

# Execução principal
if __name__ == "__main__":
    esperar_tecla()
    iniciar_programa()
