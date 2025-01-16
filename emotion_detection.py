import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using the Watson NLP Emotion Predict API.
    
    Parameters:
        text_to_analyze (str): The text that needs to be analyzed for emotions.
    
    Returns:
        str: The 'text' attribute of the response object received from the API.
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
        # Send the POST request
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the response is successful
        if response.status_code == 200:
            # Return the 'text' attribute of the response
            return response.text
        else:
            # Handle error responses
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        # Handle exceptions (e.g., network issues or API errors)
        return str(e)