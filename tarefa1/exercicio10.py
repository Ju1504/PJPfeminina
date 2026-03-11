estoque = int(input("digite o valor do estoque"))
vendas = int(input("digite o valor das vendas"))
estoque -= vendas
reposicao = int(input("digite o valor da reposição"))
estoque += reposicao
estoque %=6
print("o estoque é " + str(estoque))