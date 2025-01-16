import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text and returns the scores and dominant emotion.
    
    Parameters:
        text_to_analyze (str): The text that needs to be analyzed for emotions.
    
    Returns:
        dict: A dictionary with the scores of emotions and the dominant emotion.
    """
    # API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the response is successful
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
            
            return result
        else:
            # Handle unsuccessful responses
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        # Handle exceptions (e.g., network issues or API errors)
        return {"error": str(e)}

# Example usage
result = emotion_detector("I love this new technology.")
print(result)