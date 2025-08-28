@@ -0,0 +1,13 @@
# Exercício 3 - Quem gastou mais dinheiro?
gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("João gastou mais:", total_joao)
elif total_pedro > total_joao:
    print("Pedro gastou mais:", total_pedro)
else:
    print("Os dois gastaram o mesmo valor:", total_joao)
