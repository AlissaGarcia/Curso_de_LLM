# Curso_de_LLM

## MiniLLM - Assistente Virtual Simples em Python

Este projeto consiste no desenvolvimento de um assistente virtual simples, denominado **MiniLLM**, criado como atividade do Curso de LLM.

O objetivo do sistema é simular o funcionamento básico de um modelo de linguagem (LLM), sendo capaz de responder perguntas com base em um conjunto de respostas previamente cadastradas pelo usuário.

---

## Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

- [1] Fazer pergunta  
- [2] Ensinar nova resposta  
- [3] Listar perguntas cadastradas  
- [4] Sair  

---

## Como funciona

O MiniLLM utiliza:

- **Classe (`Robozinho`)** para representar o assistente
- **Dicionário (`dict`)** para armazenar perguntas e respostas
- **Estrutura de repetição (`while`)** para manter o sistema em execução
- **Estrutura condicional (`match case`)** para controle do menu

As perguntas são tratadas com:
- `lower()` → padronização de texto
- `strip()` → remoção de espaços extras

---

## Lógica do sistema

- Quando o usuário faz uma pergunta:
  - Se existir no banco → retorna a resposta
  - Caso contrário → informa que não sabe responder

- O usuário pode ensinar novas respostas, que são armazenadas dinamicamente

---

## ▶ Como executar

1. Certifique-se de ter o Python instalado
2. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
Execute o programa: python MiniLLM.py

--Autora
Alissa Garcia Moreira
IFCE Campus Boa Viagem
Curso: Análise e Desenvolvimento de Sistemas (ADS) <[^^]/