from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
     {
        "inputs": 11,
        "category": "YouTuber",
        "word": "TecnoGamerz"
    },
    {
        "inputs": 10,
        "category": "Asian Country",
        "word": "SouthKorea"
    },
    {
        "inputs": 6,
        "category": "Rapper",
        "word": "Eminem"
    },
    {
        "inputs":14,
        "category": "Pop Band",
        "word": "ImagineDragons"
    },
    {
        "inputs": 9,
        "category": "An element",
        "word": "Strontium"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
