import subprocess
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

def run_backend():
    """Roda o servidor Flask (backend)."""
    print("Iniciando o backend Flask...")

    # Recupera o caminho do Flask e Python a partir do .env
    VENV_PATH = os.getenv("VENV_PATH")
    DATA_BASE_SERVER = os.getenv("DATA_BASE_SERVER")
    PLN_SERVER = os.getenv("PLN_SERVER")

    # Inicializa o primeiro servidor
    process_server1 = subprocess.Popen(
        [VENV_PATH, DATA_BASE_SERVER]
    )
    
    # Inicializa o segundo servidor
    process_server2 = subprocess.Popen(
        [VENV_PATH, PLN_SERVER]
    )

    return process_server1, process_server2

if __name__ == "__main__":
    try:
        process_server1, process_server2 = run_backend()
        process_server1.wait()
        print("Servidor Database rodadndo...")
        process_server2.wait()
        print("Servidor PLN rodando...")

    except KeyboardInterrupt:
        print("\nInterrompendo processos...")
