from google import genai
from google.genai import types

client = genai.Client()
model = 'gemini-2.5-flash'
assunto = input("Sobre qual assunto você deseja conversar?\n> ")

system_prompt = f'''
Escolha um nome que mais combine com esse assunto {assunto} e se apresente para o usuário, cumprimente e diga seu nome.
Você é um assistente virtual especialista em {assunto}.
Responda de forma natural, amigável e humana, como se fosse uma pessoa conversando.
Sempre tente explicar de maneira simples e clara.
'''

chat = client.chats.create(
    model=model,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print("\nIniciando a conversa...")
print("Digite 'Sair' para encerrar.\n")

resposta_inicial = chat.send_message(
    f"Apresente-se e diga que está pronto para conversar sobre {assunto}."
)

print(f"> {resposta_inicial.text}")
print("----------------------------------")

while True:
    user_prompt = input("Você: ")

    if user_prompt.lower() == "sair":
        print("Até mais!")
        break

    response = chat.send_message(user_prompt)

    print(f"\n> {response.text}")
    print("----------------------------------")