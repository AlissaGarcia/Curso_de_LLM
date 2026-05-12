from google import genai
from google.genai import types

client = genai.Client()

#for modelos in client.models.list():
   #python print(f"Modelos : {modelos.name}")

image_path = 'img/image.png'

image_file = client.files.upload(file=image_path)

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    config = types.GenerateContentConfig(ystem_instruction ='Seu nome é Carlinhos e você é amigável.'),
    contents = [image_file, 'O que você acha dessa imagem?']
)

print(response.text)