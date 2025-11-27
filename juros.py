from datetime import datetime

JUROS_DIA = 0.025

while True:
    print("\nCALCULADORA DE JUROS - TARGET SISTEMAS")
    print("Digite 0 para sair.\n")

    valor_str = input("Digite o valor original da dívida (sem vírgula): R$ ")

    if valor_str == "0":
        print("\nSistema encerrado. Até mais!")
        break

    try:
        valor_original = float(valor_str)
    except ValueError:
        print("Valor inválido.")
        continue

    data_str = input("Digite a data de vencimento (DD/MM/AAAA): ")

  
    try:
        data_venc = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        continue

    hoje = datetime.now()

    dias_atraso = (hoje - data_venc).days

    if dias_atraso <= 0:
        print("\n✔ Não há atraso. Nenhum juro será aplicado.")
        print(f"Valor final: R$ {valor_original:.2f}")
        continue

    juros_total = valor_original * JUROS_DIA * dias_atraso
    valor_final = valor_original + juros_total

    print(f"\nDias de atraso: {dias_atraso}")
    print(f"Juros aplicados ({JUROS_DIA * 100}% ao dia): R$ {juros_total:.2f}")
    print(f"Valor final com juros: R$ {valor_final:.2f}")
