metros = int(input("digite o numero de metros"))
print("o numero de kilometros é " + str(int(metros //1000)))
restante = metros % 1000
print("o numero de metros restantes é " + str(restante))