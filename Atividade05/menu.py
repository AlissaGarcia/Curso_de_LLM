from google import genai
from google.genai import types

client = genai.Client()

model = 'gemini-2.5-flash'
system_prompt = 'Seu nome é Carlinhos e você é amigável'

while True:
    print('[1] Conversar com o Carlinhos\n[2] Pedir para o Carlinhos avaliar uma imagem.\n')
    user_input = int(input('> '))

    if(user_input == 1):
        chat = clien.chats.create(model = model, config = types.GenerateContentConfig(system_instruction= system_prompt))
        print('conversa com Carlinhos')
        user_prompt = input('>')
        print('----------------------------------')
        response = chat.send_mensage(user_prompt)
        print(response.text)
        print("---------------------------------")
    
    elif(user_input == 2):
        image_path = input('Digite o caminho até a imagem para o Carlinhos avaliar: ')
        image_file = client.files.upload(files = image_path)
        response = Client.models.generate_content(
            model= 'gemini-2.5-flash',
            config=types.GenerateContentConfig(system_instruction = system_prompt),
            contents = [image_file, 'Avalie a imagem enviada pelo usuário.']
        )
    
    else:
        print(f"erro")
    
    print(response.text)