from flask import Flask, request, jsonify
import numpy as np
import pickle
from urlanalyzer import FeatureExtraction
from flask_cors import CORS
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

# Load the trained Gradient Boosting Classifier
with open("models/model.pkl", "rb") as file:
    gbc = pickle.load(file)

def check_phishing_probability(url_input):
    """
        Check the probability of a URL being a phishing website

        Parameters:
        url_input(str): The URL to be checked.

        Returns:
        str: Message indicating the probability of the URL being safe or unsafe
    """
    try:
        # Strip any leading/trailing whitespace from the URL
        url = url_input.strip()

        # Extract features from the URL
        obj = FeatureExtraction(url)
        features = np.array(obj.getFeaturesList()).reshape(1,30)

        # Get predicition probabilities
        probabilities = gbc.predict_proba(features)[0]
        y_phishing = probabilities[0]
        y_non_phishing = probabilities[1]

        # Determine and return the probability of the URL being safe or unsafe
        if y_non_phishing > y_phishing:
            return {"message" : f"This website is {round(y_non_phishing * 100, 2)}% safe."}
        else:
            return {"message" : f"This website is {round(y_phishing * 100, 2)}% unsafe."}

    except Exception as e:
        # Return error message if an exception occur
        print(f"Error occurred: {e}")
        return {"error" : str(e), "message" : "An error occurred while processing the URL."}

@app.route('/')
def home():
    return "API is Running"

@app.route('/check-url', methods=['POST'])
def check_url():
    """
    Flask route handler for checking phishing probability of a given URL

    Expects a JSON payload with a 'url' key.
    """
    try:
        # Get the JSON data from the POST request
        data = request.get_json()

        if not data or 'url' not in data:
            return jsonify({"error" : "No URL provided in the request"}), 400
        
        # Extract the URL from the JSON data
        url_input = data['url']

        # Use the check_phishing_probability function to get the result
        result = check_phishing_probability(url_input)

        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error" : str(e), "message" : "An error occured while processing the URL"}), 500

if __name__ == '__main__':
    app.run(debug=True)   
