from flask import Flask
import random
app = Flask(__name__)



# Quotes data
quotes = [
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
    {"quote": "Get busy living or get busy dying.", "author": "Stephen King"}
]

@app.route('/get_quote')
def get_quote():
    quote = random.choice(quotes)
    return f'<h1> {quote["quote"]} </h1>'