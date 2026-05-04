from datetime import date, datetime

def parse_date_pt(s: str) -> date:
    return datetime.strptime(s, "%d-%m-%Y").date()   

def valid_vazio(s: str) -> str:
    while True:
        valor = input(f"Insira {s}: ").strip()
        if valor:
            return valor
        print(f"{s} não pode ser vazio. Por favor, insira um valor válido.")

def valid_date(s: str) -> date:
    while True:
        try:
            dt_str = input(f"Insira {s} (dd-mm-aaaa): ").strip()
            return parse_date_pt(dt_str)
        except ValueError:
            print("Formato de data inválido. Por favor, use dd-mm-aaaa.")

def valid_duplicado(s: str, existing_values: list) -> str:
    while True:
        valor = valid_vazio(s)
        if valor not in existing_values:
            return valor
        print(f"{s} '{valor}' já existe. Por favor, insira um valor único.")            