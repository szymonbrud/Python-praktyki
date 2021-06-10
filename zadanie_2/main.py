from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/")
def main():

    text = '''
        <h3>Hello, This is animal API</h3> 

        /animals - returns all animal names
        <br/>
        /cat - information about cat
        <br/>
        /dog - information about dog
        <br/>
        /mouse - information about mouse
        <br/>

    '''

    return text


@app.route('/animals')
def allAnimals():
    return jsonify(animals=['cat', 'dog', 'mouse'])


@app.route('/cat')
def cat():
    return jsonify(name='cat', cluster='mammals', numberOfLegs=4)


@app.route('/dog')
def dog():
    return jsonify(name='dog', cluster='mammals', numberOfLegs=4)


@app.route('/mouse')
def mouse():
    return jsonify(name='mouse', cluster='mammals', numberOfLegs=4)


if __name__ == "__main__":
    app.run(debug=True)
