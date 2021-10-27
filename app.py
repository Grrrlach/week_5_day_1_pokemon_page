from flask import Flask, render_template, request
app = Flask(__name__)
import requests


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        name = request.form.get('pokemon')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        print (url)
        response = requests.get (url)
        if response.ok:
            #the request worked
            if not response.json():
                return "We had an error loading your data likely the Pokemon is not in the database"
            data = response.json()
                
            poke_dict={
                'poke_name': data ['forms'][0] ['name'],
                'hp_base': data ['stats'][0] ['base_stat'],
                'attack_base': data ['stats'][1] ['base_stat'],
                'defense_base': data ['stats'][2] ['base_stat'],
                'front_shiny_sprite': data ['sprites']['front_shiny']
            }
            print(poke_dict)
            return render_template('pokemon.html.j2', pokemon_stats = poke_dict)
        else:
            return "Ain't gonna catch that 'un! That's no pokemon. Go back to search again!"
            #the request failed
                #format is: name inside of my html = name in python
    return render_template("pokemon.html.j2")
