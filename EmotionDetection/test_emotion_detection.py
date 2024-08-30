from emotion_detection import emotion_detector

# Define test cases: each test case is a tuple with a statement and the expected dominant emotion
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear")
]

# Function to run the tests
def run_tests():
    for statement, expected_emotion in test_cases:
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']
        print(f"Statement: '{statement}'")
        print(f"Expected: {expected_emotion}, Detected: {dominant_emotion}")
        assert dominant_emotion == expected_emotion, f"Test failed for: {statement}"

if __name__ == "__main__":
    run_tests()
    print("All tests completed.")