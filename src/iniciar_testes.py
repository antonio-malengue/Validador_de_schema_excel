from matar_processo import matar_processo
import subprocess


def executar_testes():
    matar_processo()
# Executar os testes com pytest
    subprocess.run(["pytest", "tests", "-v"])


if __name__ == "__main__":
    executar_testes()