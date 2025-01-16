import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text and returns a pretty-printed JSON string with the scores and dominant emotion.
    Handles blank input gracefully by returning None for all keys if the input is empty or invalid.

    Parameters:
        text_to_analyze (str): The text that needs to be analyzed for emotions.

    Returns:
        str: A pretty-printed JSON string with the scores of emotions and the dominant emotion.
             If the input is blank or an error occurs, all values in the JSON string will be None,
             or an error message will be included in the response.
    """
    # API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Return None for all keys if input is blank
    if not text_to_analyze.strip():
        return json.dumps({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, indent=4)

    # Input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=input_json)

        # Handle API response
        if response.status_code == 200:
            # Convert response text to a dictionary
            response_json = json.loads(response.text)

            # Extract the required set of emotions
            emotions = response_json["emotionPredictions"][0]["emotion"]

            # Find the dominant emotion (highest score)
            dominant_emotion = max(emotions, key=emotions.get)

            # Prepare the output dictionary
            result = {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion
            }

            # Return the pretty-printed JSON string
            return json.dumps(result, indent=4)

        elif response.status_code == 400:
            # Handle specific bad request status
            return json.dumps({
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }, indent=4)

        else:
            # Handle other unexpected status codes
            raise Exception(f"Unexpected status code: {response.status_code}: {response.text}")

    except Exception as e:
        # Handle exceptions (e.g., network issues or API errors)
        return json.dumps({
            "error": str(e),
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, indent=4)