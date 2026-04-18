from flask import Flask, request, render_template_string
from groq import Groq
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def perguntar_llm(pergunta, sistema):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": sistema
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )
    return completion.choices[0].message.content

HTML = """
<h2>IA Personalizada</h2>

<form method="post">
    <label>Digite sua pergunta:</label><br>
    <textarea name="pergunta" placeholder="Digite aqui"></textarea><br><br>

    <label>Defina o comportamento da IA (prompt de sistema):</label><br>
    <textarea name="sistema" placeholder="Ex: Você deve responder como especialista em agricultura"></textarea><br><br>

    <button type="submit">Perguntar</button>
</form>

{% if resultado %}
<hr>
<h3>Resposta:</h3>
<p>{{ resultado }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None

    if request.method == "POST":
        pergunta = request.form["pergunta"]
        sistema = request.form["sistema"]

        
        resultado = perguntar_llm(pergunta, sistema)

    return render_template_string(HTML, resultado=resultado)


app.run(debug=True)