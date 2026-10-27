compras = []

while True:
    valor = float(input("\nDigite o valor da compra (0 para encerrar): R$ "))

    # Encerra o programa quando o valor for 0
    if valor == 0:
        break

    # Validação do valor da compra
    if valor < 0:
        print("Aviso: o valor da compra não pode ser negativo!")
        continue

    # Solicita a idade do cliente
    idade = int(input("Digite a idade do cliente: "))

    # Validação da idade
    if idade < 0:
        print("Aviso: a idade não pode ser negativa!")
        continue

    # Guarda o valor original
    valor_original = valor

    # Regra 1: desconto de 20% para clientes com 65 anos ou mais
    if idade >= 65:
        valor = valor * 0.80

    # Regra 2: desconto extra de 10% se o valor superar R$ 100
    if valor > 100:
        valor = valor * 0.90

    # Calcula o desconto total
    desconto = valor_original - valor

    # Registra a compra na lista
    compras.append({
        "original": valor_original,
        "desconto": desconto,
        "final": valor
    })

    # Exibe o resultado da compra
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor:.2f}")

quantidade = len(compras)
total_bruto = sum(compra["original"] for compra in compras)
total_descontos = sum(compra["desconto"] for compra in compras)
total_final = sum(compra["final"] for compra in compras)

print("\n===== RESUMO DO DIA =====")
print(f"Quantidade de compras: {quantidade}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("=========================")
