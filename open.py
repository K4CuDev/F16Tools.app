import os
import subprocess

def run_program(program_path):
    try:
        subprocess.run(program_path, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Wystąpił błąd podczas uruchamiania programu {program_path}: {e}")
    except Exception as e:
        print(f"Wystąpił nieznany błąd: {e}")

if __name__ == "__main__":
    # Pobierz bieżący katalog, w którym znajduje się skrypt Pythona
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Ścieżki do programów, które mają zostać uruchomione (względne)
    program_path1 = os.path.join(current_directory, "main.exe")
    program_path2 = os.path.join(current_directory, "LithiumNukerV2.exe")

    # Uruchomienie pierwszego programu
    run_program(program_path1)

    # Uruchomienie drugiego programu
    run_program(program_path2)
