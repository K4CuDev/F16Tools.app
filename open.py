import subprocess

def run_program(program_path):
    try:
        subprocess.run(program_path, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Wystąpił błąd podczas uruchamiania programu {program_path}: {e}")
    except Exception as e:
        print(f"Wystąpił nieznany błąd: {e}")

if __name__ == "__main__":
    run_program("LithiumNukerV2.exe")
    run_program("main.exe")