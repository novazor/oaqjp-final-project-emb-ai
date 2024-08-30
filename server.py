from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/emotionDetector', methods=['GET', 'POST'])
def analyze():
    # Asking for input
    statement = request.form.get('statement', '') if request.method == 'POST' else request.args.get('statement', '')

    # Running emotion detector on input
    result = emotion_detector(statement)

    # Formatting output
    response_str = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str

if __name__ == '__main__':
    # Run the Flask app on localhost with port 5000
    app.run(host='localhost', port=5000, debug=True)
