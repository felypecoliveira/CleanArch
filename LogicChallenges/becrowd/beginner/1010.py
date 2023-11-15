inputs_linha1 = input()

codigo, unidades, preco = inputs_linha1.split()

codigo = int(codigo)
unidades = int(unidades)
preco = float(preco)

pagamento_linha1 = unidades * preco

inputs_linha2 = input()

codigo2, unidades2, preco2 = inputs_linha2.split()

codigo2 = int(codigo2)
unidades2 = int(unidades2)
preco2 = float(preco2)

pagamamento_linha2 = unidades2 * preco2

total = pagamento_linha1 + pagamamento_linha2

print("VALOR A PAGAR: R$ {:.2f}".format(total))
