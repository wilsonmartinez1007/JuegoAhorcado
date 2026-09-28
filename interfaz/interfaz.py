import os
import sys
from flask import Flask, session, redirect, url_for, request, render_template_string

# Permite importar desde la carpeta "logica"
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "logica"))
from ahorcado import nueva_partida, jugar_letra, palabra_mostrada, MAX_INTENTOS

app = Flask(__name__)
app.secret_key = "ahorcado-secreto"

LETRAS = list("abcdefghijklmnñopqrstuvwxyz")


@app.route("/")
def inicio():
    if "estado" not in session:
        session["estado"] = nueva_partida()
    estado = session["estado"]

    return render_template_string(
        HTML,
        palabra_mostrada=[l if l != "_" else "" for l in palabra_mostrada(estado)],
        intentos=estado["intentos"],
        mensaje=estado["mensaje"],
        tipo=estado["tipo"],
        letras=LETRAS,
        adivinadas=estado["letras_adivinadas"],
        palabra=estado["palabra"],
        terminado=estado["terminado"],
        fallos=MAX_INTENTOS - estado["intentos"],
    )


@app.route("/letra", methods=["POST"])
def letra():
    session["estado"] = jugar_letra(session["estado"], request.form.get("letra", ""))
    return redirect(url_for("inicio"))


@app.route("/nueva")
def nueva():
    session["estado"] = nueva_partida()
    return redirect(url_for("inicio"))


HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Juego del Ahorcado</title>
<style>
  body { font-family: Arial, sans-serif; background:#1B222B; color:#E6ECF3;
         display:flex; justify-content:center; padding:30px 16px; margin:0; }
  .caja { max-width:700px; width:100%; text-align:center; }
  h1 { margin-bottom:10px; }
  svg { width:180px; }
  .frame { stroke:#E6ECF3; stroke-width:4; fill:none; stroke-linecap:round; }
  .parte { stroke:#F08A8C; stroke-width:4; fill:none; stroke-linecap:round; }
  .palabra { display:flex; justify-content:center; gap:8px; margin:20px 0; flex-wrap:wrap; }
  .slot { width:36px; height:46px; border-bottom:3px solid #E6ECF3; font-size:28px;
          font-weight:bold; text-transform:uppercase; }
  .msg { padding:10px; border-radius:6px; margin:15px 0; }
  .ok { background:#1F3A2E; color:#6FCB9C; }
  .bad { background:#43262A; color:#F08A8C; }
  .info { background:#232C37; color:#9AA6B5; }
  .teclado { display:grid; grid-template-columns:repeat(9, 1fr); gap:6px; }
  .teclado button { padding:10px 0; font-size:16px; font-weight:bold; text-transform:uppercase;
                    border-radius:6px; border:2px solid #3A4553; background:#232C37;
                    color:#E6ECF3; cursor:pointer; }
  .teclado button:hover:enabled { border-color:#E6ECF3; }
  .teclado button.acierto { background:#1F3A2E; color:#6FCB9C; border-color:#6FCB9C; }
  .teclado button.fallo { background:#43262A; color:#F08A8C; border-color:#F08A8C; }
  .nueva { display:inline-block; margin-top:20px; padding:10px 24px; background:#D9B93A;
           color:#1F2A44; font-weight:bold; border-radius:6px; text-decoration:none; }
</style>
</head>
<body>
<div class="caja">
  <h1>JUEGO DEL AHORCADO</h1>

  <svg viewBox="0 0 200 240">
    <path class="frame" d="M20 225 H140 M50 225 V20 H140 V45"/>
    {% if fallos >= 1 %}<circle class="parte" cx="140" cy="65" r="20"/>{% endif %}
    {% if fallos >= 2 %}<line class="parte" x1="140" y1="85" x2="140" y2="150"/>{% endif %}
    {% if fallos >= 3 %}<line class="parte" x1="140" y1="100" x2="112" y2="128"/>{% endif %}
    {% if fallos >= 4 %}<line class="parte" x1="140" y1="100" x2="168" y2="128"/>{% endif %}
    {% if fallos >= 5 %}<line class="parte" x1="140" y1="150" x2="116" y2="192"/>{% endif %}
    {% if fallos >= 6 %}<line class="parte" x1="140" y1="150" x2="164" y2="192"/>{% endif %}
  </svg>

  <div class="palabra">
    {% for l in palabra_mostrada %}<div class="slot">{{ l }}</div>{% endfor %}
  </div>

  <p>Intentos restantes: <b>{{ intentos }}</b></p>
  <div class="msg {{ tipo }}">{{ mensaje }}</div>

  <form method="POST" action="/letra" class="teclado">
    {% for l in letras %}
      {% set usada = l in adivinadas %}
      <button name="letra" value="{{ l }}"
        class="{% if usada and l in palabra %}acierto{% elif usada %}fallo{% endif %}"
        {% if usada or terminado %}disabled{% endif %}>{{ l }}</button>
    {% endfor %}
  </form>

  <a class="nueva" href="/nueva">Nueva palabra</a>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)