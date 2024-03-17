"""
Emotion Detection Server
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Run the Emotion Detection
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Detect text emotion and return the result
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()



# # Solution
# from flask import Flask, render_template, request
# from EmotionDetection.emotion_detection import emotion_detector

# app = Flask("Emotion Detector")

# @app.route("/emotionDetector")
# def emotion_detector_function():
#     ''' This function calls the application
#     '''
#     test_to_analyze = request.args.get('textToAnalyze')
#     response = emotion_detector(text_to_analyze)

#     if response['dominant_emotion'] is None:
#         response_text = "Invalid Input! Please try again."
#     else:
#         response_text = f"For the given statement, the system response is 'anger': \
#                     {response['anger']}, 'disgust': {response['disgust']}, \
#                     'fear': {response['fear']}, 'joy': {response['joy']}, \
#                     'sadness': {response['sadness']}. The dominant emotion is \
#                     {response['dominant_emotion']}."

#     return response_text

# @app.route("\")
# def render_index_page():
#     ''' This is the function to render the html interface
#     '''
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host = "0.0.0.0", port = 5000)