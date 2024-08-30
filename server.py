from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector  # Ensure correct import path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure 'index.html' is in the 'templates' folder

@app.route('/emotionDetector', methods=['GET', 'POST'])
def analyze():
    # Extract the text to analyze from the form or query
    statement = request.form.get('statement', '') if request.method == 'POST' else request.args.get('statement', '')

    # Use the emotion detector function to get the response
    result = emotion_detector(statement)

    # Prepare the formatted output string according to the example provided
    response_str = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the formatted response string
    return response_str

if __name__ == '__main__':
    # Run the Flask app on localhost with port 5000
    app.run(host='localhost', port=5000, debug=True)
