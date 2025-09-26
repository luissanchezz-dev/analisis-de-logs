import sys

def analizar_log(path):
    fallidos = 0
    with open(path, "r") as f:
        for linea in f:
            if "Failed password" in linea:
                fallidos += 1
    print(f"Intentos fallidos detectados: {fallidos}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python analizar_logs.py <archivo_log>")
    else:
        analizar_log(sys.argv[1])
