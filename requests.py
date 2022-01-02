import tools #local file -> tools.py

print("O que queres ver?")
print("""As opções são:
1 - Valor investido (from db.csv)""")
escolha = input()
if escolha=="1":
    print("Atualmente, estão investidos",tools.total_invested("db.csv"),"¥")
else:
    print("Opção inválida.")
