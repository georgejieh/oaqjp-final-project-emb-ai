from EmotionDetection import emotion_detector
import json

# Define test cases
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

def test_emotion_detection():
    """
    Test the emotion_detector function for various inputs and expected dominant emotions.
    """
    for statement, expected_emotion in test_cases:
        # Get the result from the emotion_detector
        result_json = emotion_detector(statement)
        
        # Parse the result
        result = json.loads(result_json)
        
        # Assert the dominant emotion matches the expected emotion
        assert result["dominant_emotion"] == expected_emotion, f"Failed for: '{statement}'"

# Run tests only if the file is executed directly
if __name__ == "__main__":
    test_emotion_detection()
    print("All tests passed successfully!")