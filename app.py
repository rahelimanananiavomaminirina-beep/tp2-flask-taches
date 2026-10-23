from flask import Flask, abort, render_template , request 
app = Flask(__name__)

taches = [
    {"id": 1, "titre": "Réviser les décorateurs",
     "priorite": "haute", "terminee": False},
    {"id": 2, "titre": "Installer Flask",
     "priorite": "normale", "terminee": True},
    {"id": 3, "titre": "Lire la doc Jinja2",
     "priorite": "basse", "terminee": False},
     {"id":4,"titre": "<b>Important</b>",
      "priorite":"haut","terminee":False}
]

@app.route("/")
def index():
    return render_template("taches.html",taches=taches)

@app.route("/taches/<int:id>")
def tache(id):
    print(type(id),id)
    for t in taches:
        if t["id"] == id:
            return t["titre"]
    abort(404)
@app.route("/taches/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        priorite = request.form.get("priorite", "normale")
        nouvel_id = max((t["id"] for t in taches), default=0) + 1
        taches.append({
            "id": nouvel_id,
            "titre": titre,
            "priorite": priorite,
            "terminee": False
        })
        return render_template("taches.html", taches=taches)
    return render_template("ajouter.html")