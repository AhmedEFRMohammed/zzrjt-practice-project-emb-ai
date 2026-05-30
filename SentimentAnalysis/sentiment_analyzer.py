"""This module generates sentiment analysis products for a provided text"""

# Import the requests library to handle HTTP requests
import json
import requests

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):
    """This function takes a text and uses the IBM Watson NLP API to analyze it"""
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Send a POST request to the API with the text and headers return response.text
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    # Return the response text from the API
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
    return {"label" : label, "score" : score}
