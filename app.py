from flask import Flask, jsonify
import random
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Quotes data
quotes_df = pd.read_csv("./assets/quotes.csv")
quotes_num = len(quotes_df)

@app.route('/quote', methods=['GET'])
def get_quote():
    random_row = random.randint(1, quotes_num)
    quote = quotes_df.loc[random_row]
    quote_data = {"quote": quote["Quote"], "author": quote["Author"]}

    # Check for NaN or empty author and replace with "Anonymous"
    if pd.isna(quote["Author"]) or quote["Author"] == "":
        quote_data["author"] = "Anonymous"

    return jsonify(quote_data)

# if __name__ == '__main__':
#     # Run the app in debug mode for live updates
#     app.run(debug=True)