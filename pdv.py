ComprasOriginais = []

ComprasFinais = []

Totaldescontos = 0

while True:
    ValCompra = float(input("Qual o valor da compra?: "))
    if ValCompra == 0:
        print(f"Compras Registradas: {len(ComprasOriginais)}")
        break
    if ValCompra < 0:
        print("Valor inválido. Tente novamente.")
        ValCompra = float(input("Qual o valor da compra?: "))
        continue

    IdadeCliente = int(input("Qual a idade do cliente?: "))
    while IdadeCliente < 0:
        print("Idade inválida. Tente novamente.")
        IdadeCliente = int(input("Qual a idade do cliente?: "))

    ValorOriginal = ValCompra 
    ComprasOriginais.append(ValorOriginal)

    DescontoIdade = ValCompra * 0.20
    DescontoValor = ValCompra * 0.10
    if IdadeCliente >= 65:
        ValCompra = ValCompra * 0.80
    if ValCompra > 100:
        ValCompra = ValCompra * 0.90
    else:
        pass
    if ValCompra != ValorOriginal:
        Totaldescontos = Totaldescontos + 1
    print(f"R${ValCompra:.2f}")
    ComprasFinais.append(ValCompra)
print(f"Quantidade de descontos aplicados: {Totaldescontos}")
DescontosAplicados = sum(ComprasOriginais) - sum(ComprasFinais)
print(f"Valor total dos descontos concedidos: {DescontosAplicados:.2f}")
print(f"Total Original: {sum(ComprasOriginais)}")
print(f"Total Final: {sum(ComprasFinais)}")