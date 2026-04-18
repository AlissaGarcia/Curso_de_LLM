IA Personalizada com Flask e Groq

Aplicação web simples em Python que permite fazer perguntas a um modelo de linguagem, definindo também o comportamento da IA via prompt de sistema.

Tecnologias
Python
Flask
Groq API
python-dotenv
Como funciona

O usuário acessa a página, digita uma pergunta e define como a IA deve responder (ex: especialista em determinada área).
A aplicação envia esses dados para o modelo e exibe a resposta.

Instalação
Clone o repositório:
git clone <url-do-repositorio>
cd <nome-do-projeto>
Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:
pip install flask groq python-dotenv
Configuração

Crie um arquivo .env na raiz do projeto:

GROQ_API_KEY=sua_chave_aqui
Execução
python app.py

A aplicação estará disponível em:

http://localhost:5000
Estrutura
app.py: aplicação principal
.env: variável de ambiente com a chave da API
Observação

Não versione o arquivo .env. Adicione-o ao .gitignore para evitar exposição de chaves sensíveis.