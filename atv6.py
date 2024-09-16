preço = float(input("Digite o preço do produto: "))

desconto = preço * 0.05
preço -= desconto
print(f"O valor com desconto é {preço}")