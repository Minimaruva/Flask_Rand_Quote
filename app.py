from flask import Flask, jsonify
import random
import pandas as pd

app = Flask(__name__)

# Quotes data
quotes_df = pd.read_csv("./assets/quotes.csv")
quotes_num = len(quotes_df)


# This decorator sets the path for the function below like http.../quote
@app.route('/quote', methods=['GET'])
def get_quote():
    random_row = random.randint(1, quotes_num)
    quote = quotes_df.loc[random_row]
    quote_data = {"quote": quote["Quote"], "author": quote["Author"]}
    return jsonify(quote_data)



if __name__ == '__main__':
    # Run the app in debug mode for live updates
    app.run(debug=True)