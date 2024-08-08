def adicionarSenha():
  with open('./base.txt', 'a') as banco:
    nome = input("- Olá! Insira o nome de usuário: ")
    senha = input("- Insira a senha de usuário: ")
    banco.write(f'{nome}, {senha}\n')

def verSenha():
  with open('./base.txt', 'r') as banco:
    linhas = banco.readlines()
    if not linhas:
      print("- Nenhuma senha cadastrada.")
    else:
      for senha in linhas:
        print(f"{senha.strip()}") 
def main():
  while True:
    choice = int(input("""
  Bem-vindo ao gerenciador de senha python!
+================================+
| 1 - Adicionar senha            |
| 2 - Ver senhas                 |
| 3 - Sair                       |
+================================+
    - """))
  
    if choice == 1:
      adicionarSenha()
    elif choice == 2:
      verSenha()
    elif choice == 3:
      break

if __name__ == "__main__":
    main()