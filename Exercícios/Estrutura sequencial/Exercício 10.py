print("Forneça abaixo as medidas da caixa em cm.")

comprimento = float(input("Qual o comprimento da caixa?\n"))
largura = float(input("Qual a largura da caixa?\n"))
altura = float(input("Qual a altura da caixa?\n"))

dimensoes = comprimento * largura * altura

print(f"O volume de uma caixa caixa com as medidas {comprimento} cm X {largura} cm X {altura} cm é de {dimensoes:.2f} cm².")
