while True:
  choice = int(input("""
  Bem-vindo ao gerenciador de senha python!
+================================+
| 1 - Adicionar senha            |
| 2 - Remover senha              |
| 3 - Ver senhas                 |
| 4 - Sair                       |
+================================+
    - """))
  
  if choice == 1:
    banco = open('./base.txt','a')

    nome = input("- Ola! Insira o nome de usuario: ")
    senha = input("- Insira a senha de usuario: ")
    banco.write(f'[{nome}, {senha}] ')
    banco.close()
    banco = open('./base.txt','r')
    conteudo = banco.readlines()
    for nome, senha in conteudo:
      print(f"{nome},{senha}")
    banco.close()

  elif choice == 3:
    banco = open('./base.txt','r')
    conteudo = banco.readlines()
    print(conteudo)
    for nome, senha in conteudo:
      print(f"{nome},{senha}")
    banco.close()