import tools #local file -> tools.py

print("O que queres ver?")
print("""As opções são:
1 - Valor investido (from db.csv)
2 - Quantidade de items de um tipo (from db.csv)""")
escolha = input()
if escolha=="1":
    print("Atualmente, estão investidos",tools.total_invested("db.csv"),"¥")
elif escolha=="2":
    print("Atualmente, tens",tools.qnt_de_("db.csv"))
else:
    print("Opção inválida.")
