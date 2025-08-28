@@ -0,0 +1,6 @@
# Exercício 5 - Segundo maior valor
numeros = [32, 10, 58, 30, 55, 12, 28, 51]

segundo_maior = sorted(set(numeros), reverse=True)[1]

print("O segundo maior valor é:", segundo_maior)
