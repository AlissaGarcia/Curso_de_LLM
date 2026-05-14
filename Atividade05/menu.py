from google import genai
from google.genai import types

client = genai.Client()

model = 'gemini-2.5-flash'
system_prompt = 'Seu nome é Carlinhos e você é amigável'

while True:
    print('[1] Conversar com o Carlinhos\n[2] Pedir para o Carlinhos avaliar uma imagem.\n')
    user_input = int(input('> '))

    if(user_input == 1):
        chat = client.chats.create(model = model, config = types.GenerateContentConfig(system_instruction= system_prompt))
        while True:
            print('conversa com Carlinhos')
            user_prompt = input('>')
            print('----------------------------------')

            if (user_prompt == 'Sair'):
                break
            response = chat.send_message(user_prompt)
            print(response.text)
            print("---------------------------------")
    
    elif(user_input == 2):
        image_path = input('Digite o caminho até a imagem para o Carlinhos avaliar: ')
        image_file = client.files.upload(file = image_path)
        response = client.models.generate_content(
            model= model,
            config=types.GenerateContentConfig(system_instruction = system_prompt),
            contents = [image_file, 'Avalie a imagem enviada pelo usuário.']
        )
    
    else:
        print(f"erro")
    
    print(response.text)