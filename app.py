# app.py
from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/getmsg/',methods=['GET'])
def respond():
    # recupérer le nom du paramètre de l'url
    name = request.args.get("name",None)

    # Pour le debugging
    print(f"Got Name : {name}")

    response = {}

    # Vérifier si l'utilisateur a bien envoyé ou saisit son nom comme prévu
    if not name:
        response["ERROR"] = "No name found , please send a name ."
        # Vérifier si l'utilisateur a saisit un nombre en lieu et place d'un nom
    elif str(name).isdigit():
        response["ERROR"] = "Name can't be Numeric ."
    # Maintenant l'utilisateur a saisit un nom valide
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform !!!!"

    # Retourner la reponse au format JSON
    return jsonify(response)


@app.route('/post/',methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)

    # On peut faire les vérifications comme faites à l'étape précédente mais ici on teste juste
    # la fonctionnalité de la méthode POST
    if param:
        return jsonify({
            "Message":f"Welcome {name} to our awesome platform !!",
            # Ajouter cette option pour distinquer la méthode POST
            "METHOD":"POST"

        })
    else:
        return jsonify({
            "ERROR":"No name found, please send a name."
        })

# A Welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!!!</h1>"


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True,port=5050,debug=True)