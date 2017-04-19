"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    wantcompliment = request.args.get("wantcompliment")

    if wantcompliment:
        compliment = sample(AWESOMENESS, 3)
    else:
        compliment = []
    
    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Plays madlib game."""

    response = request.args.get("gameplay")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route("/madlib")
def show_madlib():

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = ", ".join(request.args.getlist("adjective"))
    verb = request.args.get("verb")
    noun2 = request.args.getlist("noun2")
    lengthofnoun2 = len(noun2)

    madlib = choice(["madlib.html", "madlib2.html", "madlib3.html"])
    
    print madlib

    return render_template(madlib, 
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            verb=verb,
                            noun2=noun2,
                            length=lengthofnoun2)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
