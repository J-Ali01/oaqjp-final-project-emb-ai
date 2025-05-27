import requests
import json

def emotion_detector(text_to_analyze):
    # URL of emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document" : {"text" : text_to_analyze} }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        # Extract emotion scores from the nested response
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Create a dictionary with all the emotion scores
        dominant_emo = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }

        # Find the dominant emotion (the one with the highest score)
        dominant_emotion = max(dominant_emo, key=dominant_emo.get)

    # If the response is not successful (e.g., status code 400), set emotions to None
    elif response.status_code == 400:
        anger = disgust = fear = joy = sadness = None
        dominant_emotion = None

    # Return the emotions and the dominant emotion
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }