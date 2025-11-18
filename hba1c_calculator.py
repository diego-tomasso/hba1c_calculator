while True:
    entrada: str = input("Ingrese mg/dl: ")
    if entrada.capitalize() == "Q":
        break
    glucosa_mgdl: int = int(entrada)
    glucosa_hba1c: float = (glucosa_mgdl + 46.7) / 28.7

    print(f"Su HBA1c es: {glucosa_hba1c:.2f}%")