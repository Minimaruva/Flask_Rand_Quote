# Random Quote Generator

An example project to learn how to build and deploy a simple Flask API that serves random quotes.

## Description

A Flask-based web application that provides random quotes from a CSV file. It demonstrates how to create a RESTful API, handle data with Pandas, and deploy the application on platforms like PythonAnywhere.

## Features

- **Random Quote API:** Fetches a random quote and its author.
- **Frontend Integration:** Simple HTML + inline CSS frontend to display quotes.
- **Deployed** Configured for deployed on PythonAnywhere.

## Acknowledgments

- Quotes CSV sourced from [Jakub Petriska's Gist](https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Minimaruva/Flask_Rand_Quote/tree/main
   cd Flask_Rand_Quote
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask App Locally**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

2. **Access the Frontend**
   Open `index.html` in your web browser to interact with the Random Quote Generator.

## Deployment

The application can be deployed on [PythonAnywhere](https://www.pythonanywhere.com/):

1. **Sign Up and Log In to PythonAnywhere.**
2. **Create a New Web App** and choose Flask as the framework.
3. **Upload Your Project Files** to PythonAnywhere.
4. **Set Up the Virtual Environment** and install dependencies.
5. **Configure the Web App Settings** to point to your `app.py`.


### GIF Demo

![til](assets/demo.gif)
* Random Quote Generator Interface*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Vlad Yahnon** - [minimaruva](https://github.com/Minimaruva)

