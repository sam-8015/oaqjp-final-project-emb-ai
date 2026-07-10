"""
Unit tests for the EmotionDetection package.
"""

from EmotionDetection import emotion_detector


def test_emotions():
    """
    Test the dominant emotion for various input statements.
    """

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected in test_cases.items():
        response = emotion_detector(statement)
        actual = response["dominant_emotion"]

        if actual == expected:
            print(f"PASSED: {statement}")
        else:
            print(
                f"FAILED: {statement}\n"
                f"Expected: {expected}, Got: {actual}"
            )


if __name__ == "__main__":
    test_emotions()