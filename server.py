from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the main page (index.html).
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    """
    Endpoint for emotion detection. Processes a GET request with a statement
    and returns the formatted response. Handles blank or invalid input gracefully.
    """
    # Get the input text from the query parameters
    statement = request.args.get('textToAnalyze', '').strip()

    # If the statement is empty, return a formatted plain text error message
    if not statement:
        return "Invalid text! Please try again!"

    # Process the statement using the emotion_detector function
    emotion_result = json.loads(emotion_detector(statement))

    # Check if the dominant emotion is None (indicating invalid input or error)
    if emotion_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Format the response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, 'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and 'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )

    # Return the formatted response as plain text
    return formatted_response

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)