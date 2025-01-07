from flask import Flask
import random
import pandas as pd

app = Flask(__name__)

# Quotes data
quotes_df = pd.read_csv("./assets/quotes.csv")
quotes_num = len(quotes_df)


@app.route('/')
def hello():
    greet = '<h1>This is a random quote generator!</h1>'
    link = '<p><a href="/get_quote">Get quote!</a></p>'
    return greet + link

# This decorator sets the path for the function below like http.../get_quote
@app.route('/get_quote')
def get_quote():
    random_row = random.randint(1, quotes_num)
    quote = quotes_df.loc[random_row]
    link = '<br><p><a href="/get_quote">Get new quote!</a></p>'
    return f'<h1> {quote["Quote"]} </h1><br><p>{quote["Author"]}<p>' + link



if __name__ == '__main__':
    # Run the app in debug mode for live updates
    app.run(debug=True)