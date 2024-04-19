from iniciar_testes import matar_processo as mp
import subprocess


def executar_interface():
    #mata o processo antes de rodar a interface
    mp()
    # Executar os testes com pytest
    comando = "streamlit run src/app.py"
    #subprocess.run(comando, shell=True)
    subprocess.run(["streamlit", "run", "src/app.py"])


if __name__ == "__main__":
    executar_interface()