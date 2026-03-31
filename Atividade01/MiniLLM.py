#Atividade  - Introdução a Python - Alissa Garcia Moreira, IFCE Campus Boa Viagem, ADS S4

class Robozinho:
  def __init__(self, nome):
    self.nome = nome
    self.respostas_salvas = {}

  def responder(self, pergunta):
    pergunta = pergunta.lower().strip()

    if pergunta in self.respostas_salvas:
      print("<[^-^]> | ", self.respostas_salvas[pergunta])

    else:
      print("<[T-T]> | Ainda não sei responder a essa pergunta, teste a função Ensinar Nova Resposta!")

  def ensinar_nova_resposta(self, pergunta, resposta):
    pergunta = pergunta.lower().strip()
    self.respostas_salvas[pergunta] = resposta
    print("<[^-^]/ | Aprendi uma resposta nova! Teste a função Fazer Pergunta!")

  def listar_perguntas_cadastradas(self):
    if len(self.respostas_salvas) == 0:
      print("[-_-] | Nenhuma pergunta cadastrada! Teste a função Ensinar Nova Resposta")

    else:
      print("<[°-°]> | Lista de perguntas cadastradas: \n")
      for pergunta, resposta in self.respostas_salvas.items():
        print("-", pergunta, "→", resposta)

def menu():
    robozinho = Robozinho("MiniLLM")

    while True:
      print("\n Menu MINILLM: ")
      print("[1] Fazer pergunta")
      print("[2] Ensinar Nova Resposta")
      print("[3] Listar perguntas")
      print("[4] Sair")

      try: op = int(input("> "))

      except:
        print("Digite um número válido!!")
        continue

      match op:
        case 1:
          pergunta = input("Digite sua pergunta > ")
          robozinho.responder(pergunta)

        case 2:
          pergunta = input("Digite sua pergunta > ")
          resposta = input("Digite a resposta > ")
          robozinho.ensinar_nova_resposta(pergunta, resposta)

        case 3:
          robozinho.listar_perguntas_cadastradas()

        case 4:
          print("[-_-] | Encerrando...")
          print("Encerrado!")
          break

        case _:
          print("Opção Inválida!!")
print("\nBem vindo(a)! <[0-0]/")
menu()
