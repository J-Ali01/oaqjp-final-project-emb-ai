"""
Flask application for emotion detection.
This app takes text input from the user, analyzes emotions using the EmotionDetection package,
and returns the emotion scores and dominant emotion.
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function receives text from the HTML interface, analyzes the emotions 
    using the emotion_detector() function from EmotionDetection, and returns
    the emotion scores along with the dominant emotion.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return " Invalid text! Please try again!."
    # pylint: disable=line-too-long
    return f"'anger' : {anger}, 'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy} and 'sadness' : {sadness}. The dominant emotion is {dominant_emotion}."
    # pylint: enable=line-too-long
@app.route("/")
def render_index_page():
    """
    This function renders the main application page.
    It simply serves the HTML template for the emotion analysis interface.
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
