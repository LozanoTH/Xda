from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta para votar
@app.route("/", methods=["GET", "POST"])
def votar():
    if request.method == "POST":
        candidato = request.form.get("candidato")
        if candidato:
            with open("votos.txt", "a") as f:
                f.write(candidato + "\n")
        return redirect("/resultados")
    return render_template("index.html")

# Ruta para ver resultados
@app.route("/resultados")
def resultados():
    votos = {}
    try:
        with open("votos.txt", "r") as f:
            for linea in f:
                candidato = linea.strip()
                votos[candidato] = votos.get(candidato, 0) + 1
    except FileNotFoundError:
        pass
    return render_template("resultados.html", votos=votos)

if __name__ == "__main__":
    app.run(debug=True)
