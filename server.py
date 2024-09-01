"""
Flask application for emotion detection.
Provides a web interface for users to input text
and analyze the emotions in the text using the Watson NLP API.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page with a form for user input.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def analyze():
    """
    Handles emotion analysis for user input.
    Accepts both GET and POST requests to analyze the input text.
    Returns the formatted result or an error message for invalid inputs.
    """
    # Get the input statement from the user based on the request method
    if request.method == 'POST':
        statement = request.form.get('statement', '')
    else:
        statement = request.args.get('statement', '')

    # Check for empty input
    if not statement:
        return "Invalid text! Please try again."

    # Run the emotion detection function
    result = emotion_detector(statement)

    # Handle errors from the emotion detection function
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the output response string
    response_str = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str

if __name__ == '__main__':
    # Run the Flask app on localhost with port 5000
    app.run(host='localhost', port=5000, debug=True)
