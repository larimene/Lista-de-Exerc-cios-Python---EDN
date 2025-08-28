@@ -0,0 +1,8 @@
# Exercício 4 - Maior e menor palavra
palavras = ["python", "asimov", "código", "web", "programação"]

maior = max(palavras, key=len)
menor = min(palavras, key=len)

print("Maior palavra:", maior)
print("Menor palavra:", menor)
