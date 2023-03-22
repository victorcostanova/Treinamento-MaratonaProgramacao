valor = float(input())

if valor <= 2000.00:
    print("Isento")
elif valor > 2000 and valor <= 3000:
    imposto = (valor - 2000.00) * 0.08
    print("R$","%.2f" %imposto)
elif valor > 3000 and valor <= 4500:
    imposto = (valor - 3000) * 0.18 + (1000 * 0.08)
    print("R$","%.2f" %imposto)
else:
    imposto = (valor - 4500) * 0.28 + (1000 * 0.08) + (1500 * 0.18)
    print("R$","%.2f" %imposto)