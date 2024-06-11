import numpy as np
import pickle
import warnings
from urlanalyzer import FeatureExtraction

warnings.filterwarnings('ignore')

# Load the trained Gradient Boosting Classifier
with open("models/model.pkl", "rb") as file:
    gbc = pickle.load(file)

def check_phishing_probability(url_input):
    """
    Check the probability of a URL being a phishing website.

    Parameters:
    url_input (str): The URL to be checked.

    Returns:
    str: Message indicating the probability of the URL being safe or unsafe.
    """
    try:
        url = url_input.strip()  
        obj = FeatureExtraction(url)
        features = np.array(obj.getFeaturesList()).reshape(1, 30)
        y_phishing = gbc.predict_proba(features)[0, 0]
        y_non_phishing = gbc.predict_proba(features)[0, 1]

        if y_non_phishing > y_phishing:
            return f"This website is {round(y_non_phishing * 100, 2)}% safe."
        else:
            return f"This website is {round(y_phishing * 100, 2)}% unsafe."
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing the URL."  # Return error message if an exception occurs

# Test the function with a sample URL
print(check_phishing_probability("http://att-yahoo-mail-106889.weeblysite.com/"))
