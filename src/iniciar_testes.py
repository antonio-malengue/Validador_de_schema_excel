import subprocess

def matar_processo():
    # Encontrar o PID do processo na porta 8501
    resultado = subprocess.run(["netstat", "-aon"], capture_output=True, text=True)
    linhas = resultado.stdout.splitlines()
    pid = None
    for linha in linhas:
        if ":8501" in linha:
            pid = linha.split()[-1]
            break
    # Matar o processo com o PID encontrado
    if pid:
        subprocess.run(["taskkill", "/F", "/PID", pid])

def executar_testes():
    matar_processo()
# Executar os testes com pytest
    subprocess.run(["pytest", "tests", "-v"])


if __name__ == "__main__":
    executar_testes()